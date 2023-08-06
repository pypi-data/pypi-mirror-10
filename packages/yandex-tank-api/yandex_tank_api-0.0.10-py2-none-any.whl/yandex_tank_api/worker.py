"""
Tank worker process for yandex-tank-api
Based on ConsoleWorker from yandex-tank
"""

import signal
import fnmatch
import logging
import os
import os.path
import sys
import traceback
import json
import itertools as itt
from pkg_resources import resource_filename

NEW_TANK = True

try:
    import yandextank.core as tankcore
except ImportError:
    # in case of old tank version
    sys.path.append('/usr/lib/yandex-tank')
    import tankcore #pylint: disable=F0401
    NEW_TANK = False

# Yandex.Tank.Api modules

# Test stage order, internal protocol description, etc...
import yandex_tank_api.common as common


class InterruptTest(BaseException):
    """Raised by sigterm handler"""
    def __init__(self, remove_break=False):
        self.remove_break = remove_break 

class TankCore(tankcore.TankCore):
    """
    We do not use tankcore.TankCore itself
    to let plugins know that they are executed under API server.

    Typical check in the plugin looks like this:

    def _core_with_tank_api(self):
        core_class = str(self.core.__class__)
        return core_class == 'yandex_tank_api.worker.TankCore'
    """
    def __init__(self, tank_worker):
        super(TankCore, self).__init__()
        self.tank_worker = tank_worker

    def publish(self, publisher, key, value):
        super(TankCore, self).publish(publisher, key, value)
        self.tank_worker.report_status()


class TankWorker(object):

    """    Worker class that runs tank core until the next breakpoint   """

    IGNORE_LOCKS = "ignore_locks"

    def __init__(
            self, tank_queue, manager_queue, working_dir,
            session_id, ignore_machine_defaults):
        if NEW_TANK:
            logging.info("Using yandextank.core as tank core")
        else:
            logging.warning(
                "Using obsolete /usr/lib/yandex-tank/tankcore.py as tank core")

        # Parameters from manager
        self.tank_queue = tank_queue
        self.manager_queue = manager_queue
        self.working_dir = working_dir
        self.session_id = session_id
        self.ignore_machine_defaults = ignore_machine_defaults

        # State variables
        self.break_at = 'lock'
        self.stage = 'not started'
        self.failures = []
        self.retcode = None

        reload(logging)
        self.log = logging.getLogger(__name__)
        self.core = TankCore(self)

    def __add_log_file(self, logger, loglevel, filename):
        """Adds FileHandler to logger; adds filename to artifacts"""
        full_filename = os.path.join(self.working_dir, filename)

        self.core.add_artifact_file(full_filename)

        handler = logging.FileHandler(full_filename)
        handler.setLevel(loglevel)
        handler.setFormatter(logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s %(message)s"
        ))
        logger.addHandler(handler)

    def __setup_logging(self):
        """
        Logging setup.
        Should be called only after the lock is acquired.
        """
        logger = logging.getLogger('')
        logger.setLevel(logging.DEBUG)

        self.__add_log_file(logger, logging.DEBUG, 'tank.log')
        self.__add_log_file(logger, logging.INFO, 'tank_brief.log')

    def __get_configs_from_dir(self, config_dir):
        """
        Returns configs from specified directory, sorted alphabetically
        """
        configs = []
        try:
            conf_files = os.listdir(config_dir)
            conf_files.sort()
            for filename in conf_files:
                if fnmatch.fnmatch(filename, '*.ini'):
                    config_file = os.path.realpath(
                        config_dir + os.sep + filename)
                    self.log.debug("Adding config file: %s", config_file)
                    configs += [config_file]
        except OSError:
            self.log.warning(
                "Failed to get configs from %s",
                config_dir,
                exc_info=True
                )

        return configs

    def __get_configs(self):
        """Returns list of all configs for this test"""
        configs = list(itt.chain(
            [resource_filename('yandextank.core', 'config/00-base.ini')]
            if NEW_TANK else [],
            self.__get_configs_from_dir('/etc/yandex-tank/')
            if not self.ignore_machine_defaults else [],
            [resource_filename(__name__, 'config/00-tank-api-defaults.ini')],
            self.__get_configs_from_dir('/etc/yandex-tank-api/defaults'),
            self.__get_configs_from_dir(self.working_dir),
            self.__get_configs_from_dir('/etc/yandex-tank-api/override'),
            [resource_filename(__name__, 'config/99-tank-api-override.ini')],
        ))
        return configs

    def __preconfigure(self):
        """Logging and TankCore setup"""
        self.__setup_logging()
        self.core.load_configs(self.__get_configs())
        self.core.load_plugins()

    def get_next_break(self):
        """
        Read the next break from tank queue
        Check it for sanity
        """
        while True:
            msg = self.tank_queue.get()
            # Check that there is a break in the message
            if 'break' not in msg:
                self.log.error(
                    "No break specified in the recieved message from manager")
                continue
            brk = msg['break']
            # Check taht the name is valid
            if brk not in common.test_stage_order:
                self.log.error(
                    "Manager requested break at an unknown stage: %s", brk)
            # Check that the break is later than br
            elif common.is_A_earlier_than_B(brk, self.break_at):
                self.log.error(
                    "Recieved break %s which is earlier than "
                    "current next break %s", brk, self.break_at)
            else:
                self.log.info(
                    "Changing the next break from %s to %s", self.break_at, brk)
                self.break_at = brk
                return

    def report_status(
            self,
            status='running',
            dump_status=True,
            stage_completed=False
    ):
        """Report status to manager and dump status.json, if required"""
        msg = {
            'status': status,
            'session': self.session_id,
            'current_stage': self.stage,
            'stage_completed': stage_completed,
            'break': self.break_at,
            'failures': self.failures,
            'retcode': self.retcode,
            'tank_status': self.core.status,
        }
        self.manager_queue.put(msg)
        if dump_status:
            json.dump(
                msg,
                open(os.path.join(self.working_dir, 'status.json'), 'w'),
                indent=4
            )

    def process_failure(self, reason, dump_status=True):
        """
        Act on failure of current test stage:
        - log it
        - add to failures list
        - report to manager
        """
        self.log.error("Failure in stage %s:\n%s", self.stage, reason)
        self.failures.append({'stage': self.stage, 'reason': reason})
        self.report_status(dump_status=dump_status)

    def set_stage(
            self,
            stage,
            status='running',
            dump_status=True,
            stage_completed=False
    ):
        """Unconditionally switch stage and report status to manager"""
        self.stage = stage
        self.report_status(
            status, dump_status=dump_status, stage_completed=stage_completed)

    def next_stage(self, stage, dump_status=True):
        """
        Report stage completion.
        Switch to the next test stage if allowed.
        """

        self.report_status(
            'running', dump_status=dump_status, stage_completed=True)
        while not common.is_A_earlier_than_B(stage, self.break_at):
            # We have reached the set break
            # Waiting until another, later, break is set by manager
            self.get_next_break()
        self.set_stage(stage, dump_status=dump_status)

    def perform_test(self):
        """Perform the test sequence via TankCore"""

        try:
            self.next_stage('lock', dump_status=False)
            self.core.get_lock(force=False)

        except InterruptTest as exc:
            self.process_failure("Interrupted")
            self.report_status(
                status='failed', dump_status=False)
            return
        except Exception:
            self.process_failure('Failed to obtain lock', dump_status=False)
            self.report_status(
                status='failed', dump_status=False)
            return

        try:
            self.next_stage('init')
            self.__preconfigure()

            self.next_stage('configure')
            self.core.plugins_configure()

            self.next_stage('prepare')
            self.core.plugins_prepare_test()

            self.next_stage('start')
            self.core.plugins_start_test()

            self.next_stage('poll')
            self.retcode = self.core.wait_for_finish()

        except InterruptTest as exc:
            self.process_failure("Interrupted")
	    if exc.remove_break:
                self.break_at = 'finished'
        except Exception as ex:
            self.log.exception("Exception occured, trying to exit gracefully...")
            self.process_failure("Exception:" + traceback.format_exc(ex))

        finally:
            try:
                self.next_stage('end')
                self.retcode = self.core.plugins_end_test(self.retcode)

                # We do NOT call post_process if end_test failed
                # Not sure if it is the desired behaviour
                self.next_stage('postprocess')
                self.retcode = self.core.plugins_post_process(self.retcode)
            except InterruptTest as exc:
                self.process_failure("Interrupted")
                if exc.remove_break:
                    self.brek_at = 'finished'
            except Exception as exc:
                self.process_failure(
                    "Exception while finising test:" + traceback.format_exc(ex))
            finally:
                try:
                    self.next_stage('unlock')
                except InterruptTest as exc:
                    self.process_failure("Interrupted")
                    if exc.remove_break:
                        self.brek_at = 'finished'
                except Exception as exc:
                    self.process_failure(
                        "Exception while waiting for permission to unlock:" +
                        traceback.format_exc(ex))

                self.core.release_lock()
                self.set_stage('finished', stage_completed=True)
                self.report_status(
                    status='failed' if self.failures else 'success',
                    stage_completed=True)
        self.log.info("Done performing test with code %s", self.retcode)

def signal_handler(signum,_):
    """ required for everything to be released safely on SIGTERM and SIGINT"""
    if signum==signal.SIGINT:
        raise InterruptTest(remove_break=False)
    raise InterruptTest(remove_break=True)


def run(
        tank_queue,
        manager_queue,
        work_dir,
        session_id,
        ignore_machine_defaults
):
    """
    Target for tank process.
    This is the only function from this module ever used by Manager.

    tank_queue
        Read next break from here

    manager_queue
        Write tank status there

    """
    os.chdir(work_dir)
    signal.signal(signal.SIGINT,signal_handler)
    signal.signal(signal.SIGTERM,signal_handler)
    TankWorker(
        tank_queue, manager_queue, work_dir,
        session_id, ignore_machine_defaults).perform_test()

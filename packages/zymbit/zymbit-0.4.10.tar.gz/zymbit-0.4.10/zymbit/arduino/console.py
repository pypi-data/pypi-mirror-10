import logging
import time

from zymbit.linux.console import Console

from subprocess import PIPE, STDOUT, Popen

DEFAULT_HOST = 'localhost'
DEFAULT_PORT = 6571


class ArduinoConsole(Console):
    @property
    def logger(self):
        return logging.getLogger(__name__)

    def _restart_bridge(self):
        """
        Checks to see if the bridge process is running
        :return: boolean - whether the bridge was restarted
        """
        running = self._is_bridge_running()
        if not running:
            self.logger.warning('bridge not running, resetting mcu')
            status = Popen('/usr/bin/reset-mcu').wait()
            self.logger.info('reset-mcu status={}'.format(status))

            for i in range(10):  # wait for bridge to show up
                running = self._is_bridge_running()
                if running:
                    break

                time.sleep(1.0)
            else:
                self.logger.warning('bridge still not found in process listing')

            if running:  # let the bridge settle for a couple seconds
                time.sleep(2.0)

            return running

        return False

    def handle_socket_exception(self, socket_exc):
        """
        Handle the socket exception
        :param socket_exc: Exception
        """
        # try to restart the bridge on arduinos and if successful, try reopening the socket
        if self._restart_bridge():
            return self.socket

    def _is_bridge_running(self):
        """
        Check to see if bridge is running
        :return: Boolean
        """
        command = 'ps'

        proc = Popen(command, stdout=PIPE, stderr=STDOUT)
        stdout, _ = proc.communicate('')

        running = 'python -u bridge.py' in stdout

        return running

import logging
import socket

from select import select
from zymbit.connector import get_connector
from zymbit.envelope import parse_buf

BUFSIZE = 4096


class MessengerServer(object):
    def __init__(self, host, port, message_handler=None):
        self.addr = (host, port)

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.sock.setblocking(0)

        self.sock.bind(self.addr)
        self.sock.listen(128)  # max 128 clients

        self.logger.info("Listening on TCP addr={}".format(self.addr))

        self.udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_sock.bind(self.addr)

        self.logger.info("Listening on UDP addr={}".format(self.addr))

        self.connections = {}

        self.message_handler = message_handler

        self._run = True

    @property
    def logger(self):
        logger_name = '{}.{}'.format(__name__, self.__class__.__name__)
        return logging.getLogger(logger_name)

    def connect(self, info):
        conn, addr = info
        self.logger.info('%s, %s connected' % (conn, addr))

        self.connections[conn] = addr

    def disconnect(self, connection):
        addr = self.connections.pop(connection)
        self.logger.info('%s, %s disconnected' % (connection, addr))

    def fileno(self):
        return self.sock.fileno()

    def handle_message(self, client, buf):
        if self.message_handler:
            self.message_handler.handle_message(client, self.connections[client], buf)
        else:
            message = 'client={}, buf={}'.format(self.connections[client], buf)
            self.logger.info(message)

            client.send(message)

    def loop(self, select_timeout=1.0):
        # check UDP
        buf, client = self.udp_sock.recvfrom(1024)
        if buf:
            self.handle_message(client, buf)

        try:
            self.connect(self.sock.accept())
        except socket.error, exc:
            # (11, 'Resource temporarily unavailable')
            # [Errno 35] Resource temporarily unavailable
            if exc[0] not in (11, 35):
                raise

        ready, _, _ = select(self.connections, [], [], select_timeout)

        for client in ready:
            try:
                buf = client.recv(BUFSIZE)
                if buf == '':
                    self.disconnect(client)
                    continue
            except socket.error, exc:
                if exc[0] != 54: # [Errno 54] Connection reset by peer
                    raise

                self.disconnect(client)
                continue

            self.handle_message(client, buf)

        if self.message_handler:
            self.message_handler.loop()

    def quit(self):
        self.sock.close()

        # prevent getting exception where dictionary changes while looping
        connections = self.connections.keys()
        for connection in connections:
            self.disconnect(connection)

    def run(self):
        while self._run:
            self.loop()


class ConsoleMessengerServer(MessengerServer):
    port = 9628
    host = 'localhost'

    def __init__(self, host=None, port=None, message_handler=None):
        host = host or self.host
        port = port or self.port

        super(ConsoleMessengerServer, self).__init__(host, port, message_handler=message_handler)

    @property
    def connector(self):
        return get_connector()

    def handle_message(self, client, buf):
        self.connector.send(parse_buf(buf))

    def loop(self, select_timeout=0.1):
        return super(ConsoleMessengerServer, self).loop(select_timeout=select_timeout)


if __name__ == '__main__':
    import sys

    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    server = MessengerServer('localhost', 9628)
    try:
        server.run()
    except KeyboardInterrupt:
        server.quit()

from typings.auth import Auth


class Server(object):

    def __init__(self, server):
        self.host = server['host']
        self.port = server['port']
        self.connections = int(server['connections'])
        self.auth = Auth(server['auth'])

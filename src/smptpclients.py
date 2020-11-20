from util import load_yaml


class SMTPClients(object):
    def __init__(self, servers, counter, connectionPool):
        self.servers = servers
        self.counter = counter
        self.connectionPool = connectionPool


def NewSmtpClients(configFilePath: str):
    serverList = load_yaml(configFilePath)
    clients = SMTPClients(
        servers = serverList,
        counter = 0,
        connectionPool = init_connection_pool(serverList),
    )
    return clients

# TODO CONNECTION POOLS


def init_connection_pool(serverList):
    return

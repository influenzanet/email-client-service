from util import load_yaml


class SMTPClients(object):

    def __init__(self, configFilePath, counter):
        self.servers = self.load_client_configuration(configFilePath)
        self.counter = counter
        self.connectionPool = self.init_connection_pool(self.servers)

    def load_client_configuration(self, configFilePath: str):
        """
        docstring
        """
        return load_yaml(configFilePath)

    def init_connection_pool(self, serverList):
        """
        docstring
        """
        return 1

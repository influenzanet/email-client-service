import smtplib

import utils.yaml_util as yaml_util
from typings.servers import Server
from typings.connection_pool import ConnectionPool


class SMTPClients(object):

    def __init__(self, config_file_path, counter):
        self.connection_config = self.load_client_configuration(
            config_file_path)
        self.counter = counter
        self.connection_pool = self.init_connection_pool(
            self.connection_config['servers'])

    def load_client_configuration(self, configFilePath: str):
        """
        docstring
        """
        return yaml_util.load_yaml(configFilePath)

    def init_connection_pool(self, server_list):
        """
        docstring
        """
        connection_pool = []
        for server_item in server_list:
            server = Server(server_item)
            connections = [self.create_connection(
                server) for i in range(server.connections)]
            connection_pool.extend(connections)
        return ConnectionPool(connection_pool)

    def create_connection(self, server):
        """
        docstring
        """
        connection = smtplib.SMTP_SSL(host=server.host, port=server.port)
        connection.login(user=server.auth.user, password=server.auth.password)
        return connection

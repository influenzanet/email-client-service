import smtplib

import constants.constants as constants
import utils.yaml_util as yaml_util
from typings.servers import Server
from typings.connection_pool import ConnectionPool
from typings.connection import Connection


class SMTPClients(object):

    def __init__(self, config_file_path):
        self.connection_config = self.load_client_configuration(
            config_file_path)
        self.connection_pool: ConnectionPool = self.init_connection_pool(
            self.connection_config[constants.KEY_SERVERS])

    def load_client_configuration(self, configFilePath: str):
        """
        Read the server configuration file and validate the 
        existence of the required keys in the configuration
        """
        return yaml_util.load_yaml(configFilePath)

    def init_connection_pool(self, server_list) -> ConnectionPool:
        """
        Create a list of connections for each server specified in the
        server configuration file.
        """
        connection_pool = []
        for server_item in server_list:
            server = Server(server_item)
            connections = [Connection(
                server) for i in range(server.connections)]
            connection_pool.extend(connections)
        return ConnectionPool(connection_pool)

    def get_connection(self):
        return self.connection_pool.get_connection()
    
    def get_sender(self):
        return self.connection_config[constants.KEY_SENDER]

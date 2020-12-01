import threading
import smtplib

from typings.connection import Connection


class ConnectionPool(object):

    def __init__(self, pool=[Connection]):
        self.connection_pool = pool
        self.counter = 0
        self.lock = threading.Lock()

    def get_connection(self):
        self.counter = self.counter % len(
            self.connection_pool)
        connection_object = self.connection_pool[self.counter]
        self.counter += 1

        # Check if connection has not timed out and reconnect if required
        retrieved_connection = connection_object.connection
        if not retrieved_connection:
            raise Exception("Failed to fetch connection")
        if not connection_object.is_connected():
            return self.reconnect(
                connection_object)
        return retrieved_connection

    def reconnect(self, connection_object):
        return connection_object.reconnect()
        """ with self.lock:
            if not connection_object.is_connected():
                return connection_object.reconnect()
            return connection_object.connection """

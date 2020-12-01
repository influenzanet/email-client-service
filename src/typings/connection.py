import smtplib
import logging
from distutils.util import strtobool

from constants.constants import IS_AUTH_REQUIRED, MAX_RECONNECT_ATTEMPTS, INITIAL_RECONNECT_WAIT
from utils.retry import retry


class Connection(object):

    def __init__(self, server):
        self.host = server.host
        self.port = server.port
        self.user = server.auth.user
        self.password = server.auth.password
        self.connection = self.create_connection()

    @retry(Exception, total_tries=int(MAX_RECONNECT_ATTEMPTS), initial_wait=int(MAX_RECONNECT_ATTEMPTS), logger=logging)
    def create_connection(self):
        self.connection = smtplib.SMTP(host=self.host, port=self.port)
        self.connection.connect(host=self.host, port=self.port)
        self.connection.ehlo()
        if bool(strtobool(IS_AUTH_REQUIRED)):
            self.connection.login(self.user, self.password)
        return self.connection

    def is_connected(self):
        try:
            status = self.connection.noop()[0]
        except:
            status = -1
        return status == 250

    def reconnect(self):
        return self.create_connection()

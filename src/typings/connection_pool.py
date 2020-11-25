import smtplib


class ConnectionPool(object):

    def __init__(self, connections=[]):
        self.connections = connections
        self.counter = 0

    def get_connection(self):
        connection = self.connections[]
        if not connection:
            raise Exception("Message to ask caller to wait")
        if not self.is_connected(connection):
            return self.reconnect(connection)
        return connection

    def is_connected(self, connection: smtplib.SMTP_SSL):
        try:
            status = connection.noop()[0]
        except:  # smtplib.SMTPServerDisconnected
            status = -1
        return True if status == 250 else False

    def return_connection(self, connection):
        self.connections.append(connection)

    def reconnect(self, connection: smtplib.SMTP_SSL):
        # TODO Reconnect existing connection if possible
        # Retry mechanism (and timeouts)
        new_connection = smtplib.SMTP_SSL(
            host=connection._host, port=connection.default_port)
        new_connection.login(user=connection.user,
                             password=connection.password)
        return new_connection

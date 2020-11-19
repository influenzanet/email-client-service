from util import *


class SMTPClients(object):
    def __init__(self, servers, counter, connectionPool):
        self.servers = servers
        self.counter = counter
        self.connectionPool = connectionPool

def NewSmtpClients(configFilePath: str):
	serverList = loadYaml(configFilePath)
	clients = SMTPClients(
		servers = serverList,
		counter = 0,
		connectionPool = initConnectionPool(serverList),
    )
	return clients

#TODO CONNECTION POOLS
def initConnectionPool(serverList):
    return
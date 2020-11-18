import os
import grpc
import logging
import constants
from concurrent import futures
import email_client_service_pb2
import email_client_service_pb2_grpc
from random import randint
from typing import NamedTuple
from time import sleep

class EnvStruct(NamedTuple):
    port: str
    server_config_path: str
    priority_server_config_path: str


class EmailClientServicer(email_client_service_pb2_grpc.EmailClientServiceApiServicer):
    """Provides methods that implement functionality of email client server."""

    def __init__(self):
        pass

    def Status(self, request, context):
        pass

    def SendEmail(self, request, context):
        print(request.to)
        # print(request.content)
        # print(context)

        if randint(1, 100) > 75:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details('message sending failed')
        sleep(0.3)
        return email_client_service_pb2.ServiceStatus()



def readEnvironment():
    # Read Listen port 
    port = getEnv(constants.ENV_LISTEN_PORT, constants.DEFAULT_LISTEN_PORT)
    # Read default server configuration file path
    server_config_path = getEnv(constants.ENV_CONFIG_FOLDER, constants.SERVER_CONFIG_PATH) + constants.SERVER_FILE
    # Read priority server configuration file path
    priority_server_config_path = getEnv(constants.ENV_PRI_CONFIG_FOLDER, constants.PRIORITY_SERVER_CONFIG_PATH) + constants.PRIORITY_SERVER_FILE

    return EnvStruct(port, server_config_path, priority_server_config_path)

def getEnv(envKey, defaultValue):
    return os.getenv(envKey, defaultValue)

def serve(env: EnvStruct):
    listen = env.port
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    email_client_service_pb2_grpc.add_EmailClientServiceApiServicer_to_server(
        EmailClientServicer(), server
    )
    server.add_insecure_port('[::]:' + listen)
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    env = readEnvironment()
    serve(env)
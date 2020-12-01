import os
import logging
import threading
from concurrent import futures
from random import randint
from typing import NamedTuple
from time import sleep

import grpc
import smtplib
from email.message import EmailMessage

import constants.constants as constants
import grpc_service.email_client_service_pb2 as email_client_service_pb2
import grpc_service.email_client_service_pb2_grpc as email_client_service_pb2_grpc
from typings.smptpclients import SMTPClients

config = {}


class Environment(NamedTuple):
    port: str
    server_config_path: str
    priority_server_config_path: str


class EmailClientServicer(email_client_service_pb2_grpc.EmailClientServiceApiServicer):
    """Provides methods that implement functionality of email client server."""

    def __init__(self):
        self.lock = threading.Lock()
        pass

    def Status(self, request, context):
        pass

    def SendEmail(self, request, context):
        try:
            with self.lock:
                connection = self.request_connection(request.high_prio)
                connection.send_message(construct_email(request))
        except Exception as e:
            logging.error(e)
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details('message sending failed')
        return email_client_service_pb2.ServiceStatus()
        
    def request_connection(self, is_high_priority=False) -> smtplib.SMTP:
        if is_high_priority:
            return config['prio_server_configuration'].get_connection()
        return config['server_configuration'].get_connection()


def construct_email(request):
    msg = EmailMessage()
    msg.set_content(request.content)
    msg['Subject'] = request.subject
    msg['From'] = "CASE_mailer@case.com"
    msg['To'] = request.to
    msg['Cc'] = ""
    msg['Bcc'] = ""
    return msg


def read_environment():
    # Read Listen port
    port = get_env(
        constants.ENV_LISTEN_PORT, constants.DEFAULT_LISTEN_PORT)
    # Read default server configuration file path
    server_config_path = get_env(
        constants.ENV_CONFIG_FOLDER, constants.SERVER_CONFIG_PATH) \
        + constants.SERVER_FILE
    # Read priority server configuration file path
    priority_server_config_path = get_env(
        constants.ENV_PRI_CONFIG_FOLDER, constants.PRIORITY_SERVER_CONFIG_PATH) \
        + constants.PRIORITY_SERVER_FILE

    return Environment(port, server_config_path, priority_server_config_path)


def get_env(envKey, defaultValue):
    return os.getenv(envKey, defaultValue)


def int_config(env):
    config = dict(
        server_configuration=SMTPClients(
            env.server_config_path
        ),
        prio_server_configuration=SMTPClients(
            env.priority_server_config_path
        ),
    )
    return config


def serve(env: Environment):
    listen = env.port
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=3))
    server.add_generic_rpc_handlers
    email_client_service_pb2_grpc.add_EmailClientServiceApiServicer_to_server(
        EmailClientServicer(), server
    )
    server.add_insecure_port('[::]:' + listen)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    try:
        logging.basicConfig()
        env = read_environment()
        config = int_config(env)
        serve(env)
    except Exception as e:
        logging.error(e)

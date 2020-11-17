import os
import grpc
import logging
from concurrent import futures
import email_client_service_pb2
import email_client_service_pb2_grpc

from random import randint
from time import sleep


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


def serve():
    listen = '5005'

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    email_client_service_pb2_grpc.add_EmailClientServiceApiServicer_to_server(
        EmailClientServicer(), server
    )
    server.add_insecure_port('[::]:' + listen)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()

    os.environ.get('KEY_THAT_MIGHT_EXIST')
    serve()
import os, sys

HOST = ''
PORT = 3000


class Server:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

    def send_message(self, msg: str, receiver: int):
        pass

    def push_message(self):
        pass

import socket
import threading

import colorama
from colorama import Fore

from lib.client import Client


class Server:

    def __init__(self, port, cache):
        self._cache = cache
        self._port = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.bind(('0.0.0.0', port))
        self._socket.listen(1)

    def start(self):
        colorama.init()
        print(f"{Fore.CYAN}[*] Started Caching Proxy on port {self._port}")

        while True:
            client_socket, client_address = self._socket.accept()
            client = Client(client_socket, self._cache)
            thread = threading.Thread(target=client.handle_connection)
            thread.start()

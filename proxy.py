import argparse
import sys
from multiprocessing import Process

import colorama
from colorama import Fore

from lib.cache import Cache
from lib.server import Server


def main():
    parser = argparse.ArgumentParser(description='Your local caching proxy')
    parser.add_argument('-s', dest='session_file', type=str, help='Use session file')
    parser.add_argument('-p', dest='port', type=int, help='Port (Default: 5000)', default=5000)

    args = parser.parse_args()

    colorama.init()
    cache = Cache(args.session_file)
    server = Server(args.port, cache)
    process = Process(target=server.start)
    process.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print(f"{Fore.CYAN}[*] Stopping Caching Proxy")
        process.terminate()
        sys.exit(0)


if __name__ == '__main__':
    main()

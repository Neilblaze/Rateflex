import os.path
import jsonpickle
from colorama import Fore

from lib.response import Response


class Cache:
    def __init__(self, session_file=None):
        self._session_file = session_file
        self.cache_entries = {}

        if session_file:
            self._load_session()

    def get_all(self):
        return self.cache_entries

    def has(self, url, method):
        return method in self.cache_entries and url in self.cache_entries[method]

    def get(self, url, method):
        if self.has(url, method):
            return self.cache_entries[method][url]['response']
        else:
            return None

    def store(self, response: Response):
        method = response.get_request_method()
        url = response.get_request_url()

        self.cache_entries.setdefault(method, {})[url] = {
            "response": response
        }

        if self._session_file:
            with open(self._session_file, "w") as session_file:
                session_file.write(jsonpickle.encode(self.cache_entries))

    def _load_session(self):
        if self._session_file:
            if os.path.isfile(self._session_file):
                with open(self._session_file, "r") as session_file:
                    content = session_file.read()
                    if content:
                        self.cache_entries = jsonpickle.decode(content)
                        total = sum(len(entries) for entries in self.cache_entries.values())
                        print(f"{Fore.GREEN}[+] Successfully loaded {total} cache entries from previous session")
                    else:
                        print(f"{Fore.GREEN}[+] Using session file '{self._session_file}'")
            else:
                print(f"{Fore.GREEN}[+] Using session file '{self._session_file}'")

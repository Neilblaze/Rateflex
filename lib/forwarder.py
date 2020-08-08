from urllib.parse import urlparse

import requests
import urllib3
from colorama import Fore

from lib.response import Response

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Forwarder:
    SUPPORTED_METHODS = ["GET", "POST", "HEAD"]

    def __init__(self, url: str, headers: dict, method: str, body):
        self._url = url
        self._headers = self._fix_headers(headers)
        self._method = method
        self._body = body

    def forward(self) -> Response | None:
        if self._method not in self.SUPPORTED_METHODS:
            print(f"{Fore.RED}[-] HTTP method {self._method} is not implemented")
            return None

        response = self._send_request()
        if response:
            return Response(response.text, response.status_code, response.headers, self._url, self._method)

        return None

    def _send_request(self):
        request_func = getattr(requests, self._method.lower())
        return request_func(self._url, verify=False, data=self._body, headers=self._headers)

    def _fix_headers(self, headers: dict) -> dict:
        if 'Host' in headers:
            url_parsed = urlparse(self._url)
            headers['Host'] = url_parsed.hostname

            if url_parsed.port:
                headers['Host'] += f":{url_parsed.port}"

        return headers

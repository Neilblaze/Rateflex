class Response:

    def __init__(self, content: str, status: int, headers, request_url, request_method):
        self._content = content
        self._status = status
        self.request_url = request_url
        self.request_method = request_method
        self._headers = self._build_headers(headers)

    def _build_headers(self, headers):
        processed_headers = {}

        for key, value in headers.items():
            if key == 'Transfer-Encoding':
                processed_headers['Content-Length'] = len(self._content.encode())
            else:
                processed_headers[key] = value

        return processed_headers

    def get_content(self):
        return self._content

    def get_request_url(self):
        return self.request_url

    def get_request_method(self):
        return self.request_method

    def get_status(self):
        return self._status

    def get_headers(self):
        return self._headers

    def build(self):
        # Add the first line
        lines = [f"HTTP/1.1 {self._status}"]

        # Add response headers
        for key, value in self._headers.items():
            lines.append(f"{key}: {value}")

        # Add break before body
        lines.extend(["", self._content, ""])

        return '\r\n'.join(lines).encode()

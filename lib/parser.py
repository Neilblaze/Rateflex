def get_headers(request: str):
    lines = request.split('\r\n')[1:]
    headers = {}

    for line in lines:
        if not line:
            break

        key, value = line.split(":", 1)
        headers[key.strip()] = value.strip()

    return headers


def get_url(request: str):
    return request.split(" ")[1][1:]


def get_method(request: str):
    return request.split(" ")[0]


def get_body(request: str):
    body = request.split('\r\n\r\n', 1)[-1].strip()
    return body

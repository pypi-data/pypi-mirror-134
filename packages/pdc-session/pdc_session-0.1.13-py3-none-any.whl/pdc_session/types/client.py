from typing import Any


class Payload:
    username: str
    session: str

class Response:
    error: bool
    msg: str
    data: Any
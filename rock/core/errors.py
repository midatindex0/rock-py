from aiohttp import ClientResponse
from requests import Response
from typing import Union

class RockException(Exception):
    def __init__(self, resp: Union[ClientResponse, Response], *args: object) -> None:
        self.resp = resp
        super().__init__(*args)

class Rock404(RockException):
    pass

class RockUnknown(RockException):
    pass
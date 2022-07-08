import requests

from .. import models
from ..models import RockData
from ..errors import Rock404, RockUnknown


class RockSession(requests.Session):
    def __init__(self, *args, **kwargs) -> None:
        self.BASE_URL = "https://rockapi.apiworks.tech/"
        self._endpoints = {
            "rock": "rock/",
            "random": "rock/random",
            "top": "rock/top",
            "count": "rock/count",
            "rate": "rate/",
        }
        super().__init__(*args, **kwargs)

    def _get(self, url: str):
        resp = super().get(url)
        if resp.status_code == 200:
            return resp
        elif resp.status_code == 404:
            raise Rock404(resp, "Not found")
        else:
            raise RockUnknown(resp, resp.json().get('message', '')+" [Status code: "+str(resp.status_code)+']')

    def _patch(self, url, data: dict):
        resp = super().patch(url=url, data=data)
        if resp.status_code == 200:
            return resp
        elif resp.status_code == 404:
            raise Rock404(resp, "Not found")
        else:
            raise RockUnknown(resp, resp.json().get('message', '')+" [Status code: "+str(resp.status_code)+']')


    def _pack(self, resp: dict) -> RockData:
        return RockData(
            name=resp.get("name"),
            desc=resp.get("desc"),
            image=models.URL(resp.get("image")),
            rating=resp.get("rating"),
        )

    def get_rock(self, name: str) -> RockData:
        """Search a rock by name"""
        resp: dict = self._get(self.BASE_URL + self._endpoints["rock"] + name).json()
        return self._pack(resp)

    def get_random_rock(self) -> RockData:
        """Get a random rock"""
        resp: dict = self._get(self.BASE_URL + self._endpoints["random"]).json()
        return self._pack(resp)

    def get_top_rock(self) -> RockData:
        """Get a rock with rating 5"""
        resp: dict = self._get(self.BASE_URL + self._endpoints["top"]).json()
        return self._pack(resp)

    def get_rock_count(self) -> int:
        """Get total rock count in database"""
        resp: dict = self._get(self.BASE_URL + self._endpoints["count"]).json()
        return resp.get("message")

    def rate_rock(self, name: str, rating: int) -> dict:
        """Rate a rock"""
        return self._patch(
            self.BASE_URL + self._endpoints["rate"] + name, {"rating": rating}
        ).json()

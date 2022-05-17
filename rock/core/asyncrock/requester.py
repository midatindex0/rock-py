import aiohttp

from .. import models
from ..models import RockData
from ..errors import Rock404, RockUnknown


class RockSession(aiohttp.ClientSession):
    """
    Rock Session: Subclass of aiohttp.ClientSession
    """

    def __init__(self, *args, **kwargs):
        self.BASE_URL = "https://mrconos.pythonanywhere.com/"
        self._endpoints = {
            "rock": "rock/",
            "random": "rock/random",
            "top": "rock/top",
            "count": "rock/count",
            "rate": "rate/",
        }
        super().__init__(*args, **kwargs)


    async def _get(self, url: str):
        resp = await super().get(url)
        if resp.status == 200:
            return resp
        elif resp.status == 404:
            raise Rock404("Not found")
        else:
            raise RockUnknown("Unknown error")

    async def _patch(self, url, data: dict):
        resp = await super().patch(url=url, data=data)
        if resp.status == 200:
            return resp
        elif resp.status == 404:
            raise Rock404("Not found")
        else:
            raise RockUnknown("Unknown error")

    def _pack(self, resp: dict) -> RockData:
        return RockData(
            name=resp.get("name"),
            desc=resp.get("desc"),
            image=models.URL(resp.get("image")),
            rating=resp.get("rating"),
        )

    async def get_rock(self, name: str) -> RockData:
        """Search a rock by name"""
        resp: dict = await (
            await self._get(self.BASE_URL + self._endpoints["rock"] + name)
        ).json()
        return self._pack(resp)

    async def get_random_rock(self) -> RockData:
        """Get a random rock"""
        resp: dict = await (
            await self._get(self.BASE_URL + self._endpoints["random"])
        ).json()
        return self._pack(resp)

    async def get_top_rock(self) -> RockData:
        """Get a rock with rating 5"""
        resp: dict = await (
            await self._get(self.BASE_URL + self._endpoints["top"])
        ).json()
        return self._pack(resp)

    async def get_rock_count(self) -> int:
        """Get total rock count in database"""
        resp: dict = await (
            await self._get(self.BASE_URL + self._endpoints["count"])
        ).json()
        return resp.get("message")

    async def rate_rock(self, name: str, rating: int) -> dict:
        """Rate a rock"""
        return await (
            await self._patch(
                self.BASE_URL + self._endpoints["rate"] + name, {"rating": rating}
            )
        ).json()

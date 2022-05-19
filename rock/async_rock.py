from .core.asyncrock import requester as _async_requester
from .core.models import RockData

class AsyncRock:
    """Async compatible client for the Rock API.

    Usage::

        >>> from rock import AsyncRock
        >>> import asyncio
        >>> async def main():
                r = asyncRock()
                print(await r.get_rock("test"))
        >>> asyncio.run(main())
    """
    def __init__(self, *args, **kwargs) -> None:
        self._session = _async_requester.RockSession(*args, **kwargs)

    async def get_rock(self, name: str) -> RockData:
        """Gets rocks by name.

        Arguments
        ---------
        name
            The name of the rock to fetch

        Returns
        -------
        RockData
        """
        return await self._session.get_rock(name)
        
    async def get_random_rock(self) -> RockData:
        """Gets random rock.
        
        Returns
        -------
        RockData
        """
        return await self._session.get_random_rock()

    async def get_top_rock(self) -> RockData:
        """Gets a rock with a 5 rating.
        Returns
        -------
        RockData
        """
        return await self._session.get_top_rock()

    async def get_rock_count(self) -> int:
        """Gets rock count.
        Returns
        -------
        int
        """
        return await self._session.get_rock_count()

    async def rate_rock(self, name: str, rating: int) -> dict:
        """Rates a rock.
        
        Arguments
        ---------
        name: str
            The name of the rock you would like to rate
        rating: int
            The rating you would like to give the rock

        Returns
        -------
        dict
        """

        return await self._session.rate_rock(name, rating)

    async def close(self):
        """Closes the session. Requests can't be made after session is closed"""
        await self._session.close()
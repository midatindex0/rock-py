from .core.asyncrock import requester as _async_requester
from .core.models import RockData

from .core.syncrock import requester as _sync_requester

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

        `name`: str
        """
        return await self._session.get_rock(name)
        
    async def get_random_rock(self) -> RockData:
        """Gets random rock."""
        return await self._session.get_random_rock()

    async def get_top_rock(self) -> RockData:
        """Gets a rock with 5 rating."""
        return await self._session.get_top_rock()

    async def get_rock_count(self) -> int:
        """Gets rock count."""
        return await self._session.get_rock_count()

    async def rate_rock(self, name: str, rating: int) -> dict:
        """Rates a rock.
        
        `name`: str
        `rating`: int
        """
        return await self._session.rate_rock(name, rating)

    async def close(self):
        """Closes the session. Requests can't be made after session is closed"""
        await self._session.close()

class Rock:
    """Sync client for rock api
    
    Usage::
        >>> from rock import Rock
        >>> r = Rock()
        >>> print(r.get_rock("test"))
    """
    def __init__(self, *args, **kwargs) -> None:
        self._session = _sync_requester.RockSession(*args, **kwargs)

    def get_rock(self, name: str) -> RockData:
        """Gets rocks by name.

        `name`: str
        """
        return self._session.get_rock(name)
        
    def get_random_rock(self) -> RockData:
        """Gets random rock."""
        return self._session.get_random_rock()

    def get_top_rock(self) -> RockData:
        """Gets a rock with 5 rating."""
        return self._session.get_top_rock()

    def get_rock_count(self) -> int:
        """Gets rock count."""
        return self._session.get_rock_count()

    def rate_rock(self, name: str, rating: int) -> dict:
        """Rates a rock.
        
        `name`: str
        `rating`: int
        """
        return self._session.rate_rock(name, rating)

    def close(self):
        """Closes the session. Requests can't be made after session is closed"""
        self._session.close()

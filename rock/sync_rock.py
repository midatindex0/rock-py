from .core.models import RockData
from .core.syncrock import requester as _sync_requester


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

        Arguments
        ---------
        name
            The name of the rock to fetch

        Returns
        -------
        RockData
        """
        return self._session.get_rock(name)
        
    def get_random_rock(self) -> RockData:
        """Gets random rock.
        
        Returns
        -------
        RockData
        """
        return self._session.get_random_rock()

    def get_top_rock(self) -> RockData:
        """Gets a rock with a 5 rating.
        Returns
        -------
        RockData
        """
        return self._session.get_top_rock()

    def get_rock_count(self) -> int:
        """Gets rock count.
        Returns
        -------
        int
        """
        return self._session.get_rock_count()

    def rate_rock(self, name: str, rating: int) -> dict:
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
        return self._session.rate_rock(name, rating)

    def close(self):
        """Closes the session. Requests can't be made after session is closed"""
        self._session.close()

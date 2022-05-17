from dataclasses import dataclass

class URL:
    def __init__(self, url: str) -> None:
        self.url = url

@dataclass(frozen=True)
class RockData:
    name: str
    desc: str
    image: URL
    rating: int

# Rock API Wrapper

A [Rock API](https://github.com/Mr-Conos/Rock-API) wrapper written in python that supports sync aswell as async environments.

## Installation

```sh
git clone https://github.com/lonely-code-cube/rock-py
python setup.py install
```

## How to run example
```sh
python example.py
```

## Basic Usage

### Sync Wrapper
```py
from rock import Rock
r = Rock()
print(r.get_rock("crazy rock"))
print(r.get_random_rock())
print(r.get_top_rock())
print(r.get_rock_count())
print(r.rate_rock("crazy rock", 4))
r.close()
```

### Async Wrapper
```py
from rock import AsyncRock
import asyncio

async def main():
    r = AsyncRock()
    print(await r.get_rock("crazy rock"))
    print(await r.get_random_rock())
    print(await r.get_top_rock())
    print(await r.get_rock_count())
    print(await r.rate_rock("crazy rock", 4))
    await r.close()

asyncio.run(main())
```

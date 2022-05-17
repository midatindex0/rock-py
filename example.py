import asyncio

from rock import Rock, AsyncRock

def sync_rok():
    r = Rock()
    print(r.get_rock("crazy rock"))
    r.close()

async def async_rok():
    r = AsyncRock()
    print(await r.get_rock("crazy rock"))
    await r.close()

sync_rok()
asyncio.run(async_rok())

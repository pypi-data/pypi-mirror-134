# holodex

[![PyPI version](https://badge.fury.io/py/holodex.svg)](https://badge.fury.io/py/holodex)
[![PyPI downloads](https://img.shields.io/pypi/dm/holodex.svg)](https://pypi.python.org/pypi/holodex)
[![CodeFactor](https://www.codefactor.io/repository/github/ombe1229/holodex/badge)](https://www.codefactor.io/repository/github/ombe1229/holodex)
[![Github release](https://github.com/ombe1229/holodex/actions/workflows/ci.yml/badge.svg)](https://github.com/ombe1229/holodex/actions/workflows/ci.yml)

> Holodex api wrapper

## Example

```py
import asyncio
from holodex.client import HolodexClient


async def main():
    async with HolodexClient() as client:
        search = await client.autocomplete("iofi")
        channel_id = search.contents[0].value
        print(channel_id)

        channel = await client.channel(channel_id)
        print(channel.name)
        print(channel.subscriber_count)

        videos = await client.videos_from_channel(channel_id, "videos")
        print(videos.contents[0].title)

        channels = await client.channels(limit=100)

        first = channels[0]

        print(first.name)
        print(first.subscriber_count)


asyncio.run(main())


# UCAoy6rzhSf4ydcYjJw3WoVg
# Airani Iofifteen Channel hololive-ID
# 446000
# 【 Senin Produktif 】Selamat Hari Senin! May RNG God Bless Our Gacha【 iofi / イオフィ 】

```

## Installation

```
python -m pip install holodex
```

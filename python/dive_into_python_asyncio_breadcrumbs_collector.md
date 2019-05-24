# Dive into Python’s asyncio - by Breadcrumbs Collector

## Part1:

Original post at [post](https://breadcrumbscollector.tech/dive-into-pythons-asyncio-part-1/).

### Raw notes

- Asyncio from python3.6 is stable.
- Asyncio uses observation on CPU if subprogram waits for data from network
- Asyncio is not good for heavy calculations
- Asyncio uses event loop - which if runs - makes subprograms running, if not - terminates them.
- Asyncio event loop is at it's principals similar to uvloop of node.js

### Example from part1:

```python

import asyncio
import aiohttp


async def example():
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(   # 3
            get('http://httpbin.org/user-agent', session),
            get('http://httpbin.org/headers', session),
            get('http://httpbin.org/cookies', session)
        )
        print(results)


async def get(url, session):
    async with session.get(url) as resp:
        return await resp.text()


loop = asyncio.get_event_loop()  # 1
loop.run_until_complete(example())   # 2
```

## Part2

Original post at [post](https://breadcrumbscollector.tech/dive-into-pythons-asyncio-part-2/).

### Raw notes

- Rule of Thumb - **do not block the event loop**
- Use only co-operative libraries for blocking I/O operations
- Implications of not blocking event loop equals into changing some of the libraries used that could potentially block event loop (requests, psycopg2, etc)
- requests = aiohttp
- psycopg2 = asyncpg
- When some operations cannot be replaced with co-operative asyncio alternatives - move that heavy tasks into task-queue or background

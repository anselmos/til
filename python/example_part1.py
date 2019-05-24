#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © breadcrumbscollector.tech

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

#!/usr/bin/env python3
""" module containing asynchronous coroutine"""


import asyncio
import random


async def wait_random(max_delay: int = 10) ->float:
    """ async function returning the waited delay"""
    randelay: float = random.uniform(0, float(max_delay))
    await asyncio.sleep(randelay)
    return randelay

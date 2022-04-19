#!/usr/bin/env python3
"""module containing asynchronous generator"""


import asyncio
from typing import Iterator
import random


async def async_generator() -> Iterator[float]:
    """asynchronous generator coroutine"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

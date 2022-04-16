#!/usr/bin/env python3
"""module containing couroutines"""


import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """couroutine returning a list of returns"""
    task1 = asyncio.create_task(wait_random(max_delay))
    return [await task1 for _ in range(n)]

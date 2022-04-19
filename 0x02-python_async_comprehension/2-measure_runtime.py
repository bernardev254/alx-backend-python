#!/usr/bin/env python3
"""module containing a default coroutine"""


import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    start = time.perf_counter()
    tasks = await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension())
    stop = time.perf_counter()
    return (stop - start)

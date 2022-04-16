#!/usr/bin/env python3
"""module containing couroutines"""


import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """couroutine returning a list of returns"""
    task1 = task_wait_random(max_delay)
    return [await task1 for _ in range(n)]

#!/usr/bin/env python3
"""module containing asynchronous comprehenhension coroutine"""


import asyncio
from typing import List
import random


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """coroutine returning a list from async comprehension"""
    return [no async for no in async_generator()]

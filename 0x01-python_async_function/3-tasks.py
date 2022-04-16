#!/usr/bin/env python3
"""module containing a function returning asyncio task"""
import asyncio
from typing import Type


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Type[asyncio.Task]:
    """function returning asyncio task"""
    return asyncio.create_task(wait_random(max_delay))

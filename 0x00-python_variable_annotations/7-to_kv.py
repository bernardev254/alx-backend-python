#!/usr/bin/env python3
"""module containing a type annotated function"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """type annotated function returning a tuple"""
    return k, (v * v)

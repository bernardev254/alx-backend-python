#!/usr/bin/env python3
"""module containning type annotated function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """type annotated function returning list's sum"""
    sum: float = 0.0
    for elem in input_list:
        sum += float(elem)
    return sum

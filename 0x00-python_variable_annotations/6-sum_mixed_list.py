#!/usr/bin/env python3
"""module containing a type annotated function"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """type annoted function returning sum of mxd list"""
    sum: float = 0.0
    for elem in mxd_lst:
        sum += float(elem)
    return sum

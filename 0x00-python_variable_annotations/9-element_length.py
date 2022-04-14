#!/usr/bin/env python3
"""module containing type annotated function"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable
                   [Sequence]) -> List[Tuple[Sequence, int]]:
    """function returning elements of a list and their lens"""
    return [(i, len(i)) for i in lst]

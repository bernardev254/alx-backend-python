#!/usr/bin/env python3
"""module containing type annotated function"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
"""safety first function"""
    if lst:
        return any(lst[0])
    else:
        return None

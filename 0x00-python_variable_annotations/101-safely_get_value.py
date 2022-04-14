#!/usr/bin/env python3
"""module containing type annotated function"""
from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')
def safely_get_value(dct: Mapping, key[Any], default: Union
                     [T, None] = None) -> Union[Any, None]:
    """function with mapping"""
    if key in dct:
        return dct[key]
    else:
        return default

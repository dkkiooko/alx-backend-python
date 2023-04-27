#!/usr/bin/env python3
"""type-annotated function
"""
from typing import Union


def sum_mixed_list(mxld_lst: Union[int, float]) -> float:
    """sum of int and float"""
    return sum(mxld_lst)

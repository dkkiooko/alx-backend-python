#!/usr/bin/env python3
"""type-annotated function
"""
from typing import Union


def sum_mixed_list(mxld_lst: List[Union[int, float]]) -> float:
    """sum of int and float"""
    return float(sum(mxld_lst))

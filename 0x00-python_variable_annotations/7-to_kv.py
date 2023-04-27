#!/usr/bin/env python3
"""type-annotated function
"""
from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple:
    """tuple of int and float"""
    return tuple([k, v])

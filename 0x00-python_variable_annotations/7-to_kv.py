#!/usr/bin/env python3
"""type-annotated function
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """tuple of int and float"""
    return (k, v**2)

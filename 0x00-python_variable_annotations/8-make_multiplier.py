#!/usr/bin/env python3
"""type-annotated function
"""
from typing import Callable


def make_multiplier(multiplier: float, func) -> float:
    """make callable function"""
    return func(multiplier)

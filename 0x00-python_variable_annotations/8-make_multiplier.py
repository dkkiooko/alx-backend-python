#!/usr/bin/env python3
"""type-annotated function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make callable function"""
    def f(n: float) -> float:
        """multiplies float by multiplier"""
        return float(n * multiplier)
    return f

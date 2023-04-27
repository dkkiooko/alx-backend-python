#!/usr/bin/env python3
"""augment code with duck-typed annotation
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """duck type annotation"""
    if lst:
        return lst[0]
    else:
        return None

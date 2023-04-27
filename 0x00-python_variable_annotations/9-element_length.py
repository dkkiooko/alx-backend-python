#!/usr/bin/env python3
""" annotate function parameters
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Element length """
    return [(i, len(i)) for i in lst]

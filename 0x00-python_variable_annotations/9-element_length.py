#!/usr/bin/env python3
""" Basic annotations - duck type an iterable object """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Annotate the below function’s parameters and
    return values with the appropriate types:
    def element_length(lst):
    return [(i, len(i)) for i in lst]
    """
    return [(i, len(i)) for i in lst]

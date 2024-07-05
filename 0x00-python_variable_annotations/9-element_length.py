#!/usr/bin/env python3
'''
python annotations of t00.
'''
from typing import List, Union, Tuple, Callable, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    annote the function
    '''
    return [(i, len(i)) for i in lst]

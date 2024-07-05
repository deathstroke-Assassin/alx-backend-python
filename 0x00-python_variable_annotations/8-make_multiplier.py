#!/usr/bin/env python3
'''
python annotations of t00.
'''
from typing import List, Union, Tuple, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    sum of inputs.
    '''
    return lambda k: k * multiplier

#!/usr/bin/env python3
'''
python annotations of t00.
'''
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    '''
    sum of inputs.
    '''
    return (k, float(v**2))

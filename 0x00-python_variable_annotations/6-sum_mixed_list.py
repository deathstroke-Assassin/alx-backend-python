#!/usr/bin/env python3
'''
python annotations of t00.
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    sum of inputs.
    '''
    return float(sum(mxd_lst))

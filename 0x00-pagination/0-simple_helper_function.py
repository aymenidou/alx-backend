#!/usr/bin/env python3
'''0x00-pagination'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    '''The function should return a tuple of size two containing
      a start index and an end index corresponding to the range of
      indexes to return in a list for those particular pagination
      parameters.'''
    if (page == 1):
        return (0, page_size)
    first_idx = (page-1) * page_size
    return (first_idx, first_idx+page_size)

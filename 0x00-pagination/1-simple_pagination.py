#!/usr/bin/env python3
'''0x00-pagination'''
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple:
    '''The function should return a tuple of size two containing
      a start index and an end index corresponding to the range of
      indexes to return in a list for those particular pagination
      parameters.'''
    if (page == 1):
        return (0, page_size)
    first_idx = (page-1) * page_size
    return (first_idx, first_idx+page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''get a page of data from the csv file'''
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        first_idx, last_idx = index_range(page, page_size)
        data = self.dataset()
        if (first_idx > len(data)):
            return []
        return data[first_idx:last_idx]

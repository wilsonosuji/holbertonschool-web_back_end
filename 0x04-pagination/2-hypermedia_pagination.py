#!/usr/bin/env python3
"""
Simple Pagination
"""

import csv
import math
from typing import List


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
        """ Get Page
        """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0

        def index_range(page: int, page_size: int) -> tuple:
            """index"""
            return (page - 1) * page_size, page * page_size
        items = index_range(page, page_size)
        start = items[0]
        end = items[1]
        get_dataset = self.dataset()
        get_page = get_dataset[start: end]

        return get_page

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """ Get hypermedia pagination """
        my_dict = {}

        total_page = len(self.dataset()) / page_size

        my_dict['page'] = page

        my_dict['page_size'] = page_size

        my_dict['data'] = self.get_page(page, page_size)

        my_dict['next_page'] = page + 1 if total_page > page else None

        my_dict['prev_page'] = page - 1 if page != 1 else None

        my_dict['total_pages'] = math.ceil(total_page)

        return my_dict

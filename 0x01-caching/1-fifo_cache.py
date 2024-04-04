#!/usr/bin/env python3
'''0x01-caching'''
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    '''FIFOCache'''

    def __init__(self):
        """Initialize
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if (key is None or item is None):
            return

        self.cache_data[key] = item
        if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD: {}".format(first_key))

    def get(self, key):
        """ Get an item by key
        """
        if (key is None or key not in self.cache_data.keys()):
            return None
        return self.cache_data[key]

#!/usr/bin/python3
""" 0. Basic dictionary """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Create a class BasicCache that inherits
    from BaseCaching and is a caching system """

    def put(self, key, item):
        """ Put Method - assign to the dictionary """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get Method - return the value in the dictionary linked to key """
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)

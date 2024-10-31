#!/usr/bin/env python3
"""Create a class BasicCache that inherits from
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """BaseCaching class that inherits from BaseCaching
    """

    def __init__(self):
        """__init__ function that initialize the cache_data
        """
        super().__init__()

    def put(self, key, item):
        """_summary_

        Args:
                key (_type_): _description_
                item (_type_): _description_
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key

        Args:
                key (_type_): _description_
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)

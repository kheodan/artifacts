from collections import OrderedDict


class Cache:
    def __init__(self, size):
        self.cache = OrderedDict()
        self.cacheSize = size

    def __getitem__(self, key):
        value = self.cache[key]
        return self.touch(key, value)

    def __setitem__(self, key, value):
        self.touch(key, value)

    def touch(self, key, value):
        try:
            self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            self.cache[key] = value
            if len(self.cache.keys()) > self.cacheSize:
                self.cache.pop(self.cache.keys()[0])
            return value

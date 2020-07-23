import datetime

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
            res = self.cache.pop(key)['value']
            self.cache[key] = {'time': datetime.datetime.now(), 'value': value}
            return res
        except KeyError:
            self.cache[key] = {'time': datetime.datetime.now(), 'value': value}
            if len(self.cache.keys()) > self.cacheSize:
                self.cache.popitem(last=False)
                res = self.cache.pop(key)['value']
                self.cache[key] = {'time': datetime.datetime.now(), 'value': value}
                return res

# a = Cache(100)
# a['foo'] = 'bar'
# a.cache.get('foo').get('value')
# > 'bar'
#
# a.cache.get('foo').get('time')
# > datetime.datetime(2020, 7, 23, 20, 20, 5, 356122)
#
# a['foo']
# > 'bar'

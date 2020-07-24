import datetime

from collections import OrderedDict


class Cache:
    def __init__(self, size, ttl):
        self.cache = OrderedDict()
        self.cacheSize = size
        self.ttl = ttl

    def __getitem__(self, key):
        try:
            value = self.cache.get(key).get('value')
            return self.touch(key, value)
        except AttributeError:
            return None

    def __setitem__(self, key, value):
        self.touch(key, value)

    def touch(self, key, value):
        try:
            self.cache.pop(key)
            self.cache[key] = {'time': datetime.datetime.now(), 'value': value}
            return value
        except KeyError:
            self.cache[key] = {'time': datetime.datetime.now(), 'value': value}
            if len(self.cache.keys()) > self.cacheSize:
                self.cache.popitem(last=False)
                self.cache[key] = {'time': datetime.datetime.now(), 'value': value}
                return value

    def check(self, key, **kwargs):
        ttl = kwargs.get('ttl', self.ttl)
        res = self.cache.get(key, None)
        if res is not None:
            if res.get('time') > datetime.datetime.now()-datetime.timedelta(seconds=ttl):
                return res.get('value')
            else:
                self.cache.pop(key)
                return None
        else:
            return None

# size = 128
# default_ttl = 60
# a = Cache(size,default_ttl)
# a['foo'] = 'bar'
# a.cache.get('foo').get('value')
# > 'bar'
#
# a.cache.get('foo').get('time')
# > datetime.datetime(2020, 7, 23, 20, 20, 5, 356122)
#
# a['foo']
# > 'bar'
#
# a.check('foo',ttl=1500)
# > None || 'bar'
#
# a.check('foo')
# > None || 'bar'

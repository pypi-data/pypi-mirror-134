from abc import ABCMeta, abstractmethod
from diskcache import Cache

# cache component definition
class ICache(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def set(self, key, value, expire):
        pass

    @abstractmethod
    def get(self, key):
        pass

# default cache component
class DefaultCache(ICache):
    def __init__(self):
        self.cache = Cache(r'/tmp')

    def set(self, key, value, expire):
        self.cache.set(key, value, expire=expire, retry=True)

    def get(self, key):
        return self.cache.get(key)

import redis
from django.conf import settings

class RedisUtils:
    def __init__(self):
        self.cache = redis.StrictRedis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            db=settings.REDIS_DB
        )

    def get(self, key):
        return self.cache.get(key)

    def set(self, key, value, ex=None):
        self.cache.set(key, value, ex=ex)

    def delete(self, key):
        self.cache.delete(key)

    def exists(self, key):
        return self.cache.exists(key)

    def incr(self, key):
        self.cache.incr(key)

    def setex(self, key, time, value):
        self.cache.setex(key, time, value)

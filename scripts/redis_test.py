import redis
from django.conf import settings

def test_redis_connection():
    try:
        cache = redis.StrictRedis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            db=settings.REDIS_DB
        )
        cache.ping()
        print("Redis connection successful!")
    except redis.ConnectionError:
        print("Redis connection failed!")

if __name__ == "__main__":
    test_redis_connection()

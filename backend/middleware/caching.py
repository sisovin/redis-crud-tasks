import redis
from django.conf import settings
from django.core.cache.backends.base import BaseCache
from django.utils.deprecation import MiddlewareMixin

class RedisCachingMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response
        self.cache = redis.StrictRedis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            db=settings.REDIS_DB
        )

    def __call__(self, request):
        if request.method == 'GET':
            cache_key = self._generate_cache_key(request)
            cached_response = self.cache.get(cache_key)
            if cached_response:
                return self._build_response(cached_response)

        response = self.get_response(request)

        if request.method == 'GET' and response.status_code == 200:
            cache_key = self._generate_cache_key(request)
            self.cache.set(cache_key, response.content)

        return response

    def _generate_cache_key(self, request):
        return f"{request.path}_{request.GET.urlencode()}"

    def _build_response(self, cached_response):
        from django.http import HttpResponse
        return HttpResponse(cached_response)

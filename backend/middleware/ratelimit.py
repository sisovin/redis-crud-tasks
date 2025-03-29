import redis
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse

class RateLimitMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response
        self.cache = redis.StrictRedis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            db=settings.REDIS_DB
        )
        self.rate_limit = 100  # requests per minute
        self.rate_limit_window = 60  # seconds

    def __call__(self, request):
        client_ip = self._get_client_ip(request)
        if self._is_rate_limited(client_ip):
            return JsonResponse({'error': 'Rate limit exceeded'}, status=429)

        response = self.get_response(request)
        self._increment_request_count(client_ip)
        return response

    def _get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def _is_rate_limited(self, client_ip):
        request_count = self.cache.get(client_ip)
        if request_count and int(request_count) >= self.rate_limit:
            return True
        return False

    def _increment_request_count(self, client_ip):
        if self.cache.exists(client_ip):
            self.cache.incr(client_ip)
        else:
            self.cache.setex(client_ip, self.rate_limit_window, 1)

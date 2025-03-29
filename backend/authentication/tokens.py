import datetime
import jwt
from django.conf import settings
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken

def generate_jwt(user):
    payload = {
        'user_id': user.id,
        'exp': timezone.now() + datetime.timedelta(hours=1),
        'iat': timezone.now()
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token

def verify_jwt(token):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def generate_refresh_token(user):
    refresh = RefreshToken.for_user(user)
    return str(refresh), str(refresh.access_token)

def verify_refresh_token(token):
    try:
        refresh = RefreshToken(token)
        return refresh.user_id
    except Exception:
        return None

import pyotp
import base64
import os
from django.conf import settings
from django.core.cache import cache

def generate_otp(user):
    secret = base64.b32encode(os.urandom(10)).decode('utf-8')
    otp = pyotp.TOTP(secret, interval=300)
    cache.set(f'otp_{user.id}', secret, timeout=300)
    return otp.now()

def verify_otp(user, otp_code):
    secret = cache.get(f'otp_{user.id}')
    if not secret:
        return False
    otp = pyotp.TOTP(secret, interval=300)
    return otp.verify(otp_code)

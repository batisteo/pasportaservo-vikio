from .base import *


SECRET_KEY = get_env_setting('SECRET_KEY')

EMAIL_BACKEND = "sgbackend.SendGridBackend"
SENDGRID_API_KEY = get_env_setting('SENDGRID_API_KEY')
EMAIL_SUBJECT_PREFIX = '[PS vikio] '
DEFAULT_FROM_EMAIL = 'Pasporta Servo <saluton@pasportaservo.org>'

ALLOWED_HOSTS = ['vikio.pasportaservo.org']

ADMINS = (
    ('Baptiste Darthenay', 'baptiste.darthenay@gmail.com'),
)

SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

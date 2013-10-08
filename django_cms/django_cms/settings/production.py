from .base import *


DEBUG = environ.get('DJANGO_DEBUG', False)
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [
    'https://devfestitaly.herokuapp.com',
]

SITE_ID = 2

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
from .base import *  # noqa
from .base import env

DEBUG = env('DEBUG', default=False)

SECRET_KEY = env("SECRET_KEY")
STATIC_ROOT = env("STATIC_ROOT")

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS")
DATABASES["default"] = env.db("DATABASE_URL")
DATABASES["default"]["ATOMIC_REQUESTS"] = True
DATABASES["default"]["CONN_MAX_AGE"] = env.int("CONN_MAX_AGE", default=60)

INSTALLED_APPS += ["gunicorn"]  # noqa
CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS")
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

from .base import *  # noqa
from .base import env

DEBUG = False

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS")
DATABASES["default"] = env.db("DATABASE_URL")
DATABASES["default"]["ATOMIC_REQUESTS"] = True
DATABASES["default"]["CONN_MAX_AGE"] = env.int("CONN_MAX_AGE", default=60)

INSTALLED_APPS += ["gunicorn"]  # noqa
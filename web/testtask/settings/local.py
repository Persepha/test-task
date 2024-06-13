import socket

from .base import *

hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]

INSTALLED_APPS += [
    "debug_toolbar",
]
MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

DEBUG_TOOLBAR_CONFIG = {
    # IS_RUNNING_TESTS must be False even though we're running tests because we're running the toolbar's own tests.
    "IS_RUNNING_TESTS": False,
}

DB_DATABASE = os.environ.get("POSTGRES_DB")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
DB_USERNAME = os.environ.get("POSTGRES_USER")
DB_HOST = os.environ.get("POSTGRES_HOST")
DB_PORT = os.environ.get("POSTGRES_PORT")
DB_IS_AVAILABLE = all(
    [
        DB_DATABASE,
        DB_PASSWORD,
        DB_USERNAME,
        DB_HOST,
        DB_PORT,
    ]
)

if DB_IS_AVAILABLE:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": DB_DATABASE,
            "USER": DB_USERNAME,
            "PASSWORD": DB_PASSWORD,
            "HOST": DB_HOST,
            "PORT": DB_PORT,
        }
    }

LOGGING = {
    "version": 1,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {"django.db.backends": {"handlers": ["console"], "level": "DEBUG"}},
}

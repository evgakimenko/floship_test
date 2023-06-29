import environ

from .common import *

env = environ.Env()

INSTALLED_APPS += [
    'apps.warehouse',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'warehouse',
        'USER': env('WAREHOUSE_DB_USER'),
        'PASSWORD': env('WAREHOUSE_DB_PASSWORD'),
        'HOST': env('WAREHOUSE_DB_HOST'),
        'PORT': env('WAREHOUSE_DB_PORT'),
        'CONN_HEALTH_CHECKS': True,
    }
}

SESSION_COOKIE_NAME = 'warehouse_session_id'

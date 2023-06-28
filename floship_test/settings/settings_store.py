import environ

from .common import *

env = environ.Env()
environ.Env.read_env()

INSTALLED_APPS += [
    'apps.store',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'store',
        'USER': env('STORE_DB_USER'),
        'PASSWORD': env('STORE_DB_PASSWORD'),
        'HOST': env('STORE_DB_HOST'),
        'PORT': env('STORE_DB_PORT'),
        'CONN_HEALTH_CHECKS': True,
    }
}

SESSION_COOKIE_NAME = 'store_session_id'

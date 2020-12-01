from .base import *


DEBUG = False

ALLOWED_HOSTS = ['juancruzrossi.herokuapp.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}

STATICFILES_DIRS = (BASE_DIR,'static',)


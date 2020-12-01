from .base import *


DEBUG = True

ALLOWED_HOSTS = ['juancruzrossi.herokuapp.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd7pjg9hn5mg3c7',
        'USER': 'ohhlydxcblrttc',
        'PASSWORD': '37b19d98f83f046257735f512f751d2bca6117a5c4567ac10af6e76929ab751e',
        'HOST': 'ec2-3-210-23-22.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}

STATICFILES_DIRS = (BASE_DIR,'static',)
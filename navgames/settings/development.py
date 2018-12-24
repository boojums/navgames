from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'navgames',
        'USER': 'cristina',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

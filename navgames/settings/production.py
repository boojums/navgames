from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['.navigationgames.org']

SECURE_SSL_REDIRECT = True

STATIC_ROOT = "/home/boojum/navgames-static/"

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': '/home/boojum/navgames/project.db'
	}
}

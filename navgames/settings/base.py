import os

"""
Django settings for navgames project.

Generated by 'django-admin startproject' using Django 1.8.14.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/

In $VIRTUAL_ENV/bin/postactivate:
export DJANGO_SETTINGS_MODULE="navgames.settings.development"
In $VIRTUAL_ENV/bin/predeactivate
unset DJANGO_SETTINGS_MODULE
For production this needs to be set also in the wsgi.py file:
os.environ['DJANGO_SETTINGS_MODULE'] = 'navgames.settings.production'

Also set API keys as environ variables.
"""


def gettext(s):
    return s

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
with open(os.path.join(BASE_DIR, 'secret_key.txt')) as f:
    SECRET_KEY = f.read().strip()


ALLOWED_HOSTS = []


# Application definition

ROOT_URLCONF = 'navgames.urls'

WSGI_APPLICATION = 'navgames.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'America/New_York'

USE_I18N = False

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = "/var/www/navgames.org/static"

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
SITE_ID = 1


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.i18n',
                'django.core.context_processors.debug',
                'django.core.context_processors.request',
                'django.core.context_processors.media',
                'django.core.context_processors.csrf',
                'django.core.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.core.context_processors.static',
                'cms.context_processors.cms_settings',
                'aldryn_boilerplates.context_processors.boilerplate',
                'navgames.context_processors.google_analytics'
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'aldryn_boilerplates.template_loaders.AppDirectoriesLoader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader'
            ],
        },
    },
]


MIDDLEWARE_CLASSES = [
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
]

INSTALLED_APPS = [
    'djangocms_admin_style',
    'registration',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'liveresults',
    'events',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'aldryn_style',
    'djangocms_column',
    'filer',
    'aldryn_bootstrap3',
    'easy_thumbnails',
    'aldryn_apphooks_config',
    'aldryn_categories',
    'aldryn_common',
    'aldryn_newsblog',
    'aldryn_people',
    'cmsplugin_filer_image',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_utils',
    'cmsplugin_filer_video',
    'djangocms_maps',
    'djangocms_inherit',
    'djangocms_link',
    'rest_framework',
    'reversion',
    'rssplugin',
    'aldryn_reversion',
    'adminsortable2',
    'aldryn_boilerplates',
    'aldryn_translation_tools',
    'parler',
    'sortedm2m',
    'aldryn_mailchimp',
    'aldryn_faq',
    'taggit',
    'navgames',
    'django_extensions'
]

LANGUAGES = (
    ('en', gettext('en')),
)

PARLER_LANGUESG = {
    1: (
        {'code': 'en'},
    ),
    'default': {
        'fallback': 'en',
        'hide_unstranslated': False,
    }
}

# ALDRYN_BOILERPLATE_NAME = 'legacy'

CMS_LANGUAGES = {
    1: [
        {
            'code': 'en',
            'name': gettext('en'),
            'hide_untranslated': False,
            'redirect_on_fallback': True,
            'public': True,
        },
    ],
    'default': {
        'public': True,
        'hide_untranslated': False,
        'redirect_on_fallback': True,
    },
}

CMS_TEMPLATES = (
    ('page.html', 'Page'),
    ('page_notitle.html', 'Blank page (no title)'),
    ('front_page.html', 'Front page')
)

CMS_MAX_PAGE_HISTORY_REVERSIONS = 15
CMS_MAX_PAGE_PUBLISH_REVERSIONS = 10

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {
    'map': {
        'plugins': ['MapsPlugin']
    }
}


CMS_STYLE_NAMES = (
    ('feature-visual', "feature-visual"),
    ('feature-content', 'feature-content')
)

DJANGOCMS_LINK_USE_SELECT2 = True

# Save text of blog entries, not just intro
ALDRYN_NEWSBLOG_UPDATE_SEARCH_DATA_ON_SAVE = True

# Registration settings
REGISTRATION_OEPN = True
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/accounts/login/'

DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': 'localhost',
        'NAME': 'project.db',
        'PASSWORD': '',
        'PORT': '',
        'USER': ''
    }
}

MIGRATION_MODULES = {
}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
    'easy_thumbnails.processors.background'
)

# djangcms-maps settings
MAPS_PROVIDERS = [
    ('googlemaps', gettext('Google Maps (API key required)')),
]

MAPS_GOOGLEMAPS_API_KEY = os.environ.get('GOOGLEMAPS_API_KEY')

MAILCHIMP_API_KEY = os.environ.get('MAILCHIMP_API_KEY')

GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-87368514-1'
GOOGLE_ANALYTICS_DOMAIN = 'navigationgames.org'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGE_SIZE': 10
}

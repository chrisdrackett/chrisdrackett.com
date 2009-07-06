import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASE_ENGINE = 'mysql'
DATABASE_NAME = 'platypus'
DATABASE_USER = 'root'
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''

TIME_ZONE = 'UTC' # as most of our data is coming from feeds that use UTC, platypus uses UTC as well.
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False
ADMIN_MEDIA_PREFIX = '/media/'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'platypus.urls'

ROOT_PATH = os.path.dirname(__file__)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',

    # Make the media URL available everywhere
    'platypus.extras.context_processors.media',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.markup',
    'django.contrib.humanize',
    'django.contrib.admin',
    'django.contrib.webdesign',
    'tagging',
    'platypus.apps.events',
    'platypus.apps.links',
    'platypus.apps.music',
    'platypus.apps.runs'
)

EMPTY_ITEM = '---'

DELICIOUS_USERNAME = 'username'
DELICIOUS_PASSWORD = 'password'

LASTFM_KEY = 'key'
LASTFM_SECRET = 'secret'
LASTFM_USERNAME = 'username'
LASTFM_PASSWORD = 'password'
LASTFM_SESSION = ''

NIKE_PLUS_ID = 'runner_id'

try:
    from local_settings import *
except ImportError:
    pass


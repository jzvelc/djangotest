import os
import json
import dj_database_url
from datetime import timedelta
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
from django.conf.global_settings import AUTHENTICATION_BACKENDS as AB
from django.conf.global_settings import STATICFILES_FINDERS as SFF
from django.conf.global_settings import STATICFILES_DIRS as SFD
from django.utils.translation import ugettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

"""
Environment based settings
"""
ENV = os.getenv('DJANGO_ENV', os.getenv('LOCAL_DJANGO_ENV', 'development'))
STATIC_ROOT = os.getenv('DJANGO_STATIC_ROOT', os.getenv('LOCAL_DJANGO_STATIC_ROOT', os.path.join(BASE_DIR, 'data', 'static')))
MEDIA_ROOT = os.getenv('DJANGO_MEDIA_ROOT', os.getenv('LOCAL_DJANGO_MEDIA_ROOT', os.path.join(BASE_DIR, 'data', 'media')))
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'itu)*#x1n)(bnnpk+6c@si&(+!791fd&%7_ts@q&1fii!@a2$^')
REDIS_IP = os.getenv('REDIS_IP', os.getenv('LOCAL_REDIS_IP', 'localhost'))
REDIS_PORT = os.getenv('REDIS_PORT', os.getenv('LOCAL_REDIS_PORT', '6379'))

"""
Common settings
"""
ROOT_URLCONF = 'project.urls'
WSGI_APPLICATION = 'project.wsgi.application'
ADMINS = (('Jure Zvelc', 'jzvelc@gmail.com'),)
MANAGERS = ADMINS
SITE_ID = 1
SITE_URL = 'http://dlabstest.dev'
SITE_DOMAIN = 'dlabstest.dev'
SITE_NAME = 'Dlabs Test'
TIME_ZONE = 'Europe/Paris'
USE_TZ = True
USE_I18N = True
USE_L10N = True
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
AUTH_USER_MODEL = 'dlabs_users.User'

"""
Language settings
"""
LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', _('English')),
)

"""
Debug settings
"""
DEBUG = True
TEMPLATE_DEBUG = True
if ENV != 'development':
    DEBUG = False
    TEMPLATE_DEBUG = False

ALLOWED_HOSTS = [
    '.localhost',
    '.dlabstest.dev'
]

if DEBUG:
    CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_HEADERS = (
    'x-requested-with',
    'content-type',
    'accept',
    'origin',
    'authorization',
    'x-csrftoken',
    'x-token'
)

"""
Database settings
"""
DATABASES = {
    'default': dj_database_url.parse(os.getenv('DATABASE_URL', os.getenv('LOCAL_DATABASE_URL')))
}

"""
Logging settings
"""
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d '
                      '%(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        # 'mail_admins': {
        #     'level': 'ERROR',
        #     'filters': ['require_debug_false'],
        #     'class': 'django.utils.log.AdminEmailHandler'
        # }
    },
    'loggers': {
        'project': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            #'handlers': ['console', 'mail_admins'],
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

"""
App settings
"""
INSTALLED_APPS = (
    'cacheops',
    'corsheaders',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'debug_toolbar',
    'django_extensions',
    'django_redis',
    'rest_framework',
    'rest_framework_swagger',
    'project.apps.UsersConfig',
    'sorl.thumbnail',
)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'project.utils.show_debug_toolbar',
    'SHOW_COLLAPSED': False
}
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

REST_FRAMEWORK = {
    'DEFAULT_MODEL_SERIALIZER_CLASS': 'rest_framework.serializers.ModelSerializer',
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.AcceptHeaderVersioning',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'users.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),

    'DEFAULT_RENDERER_CLASSES': (
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
    ),
}

"""
Session settings
"""
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
# SESSION_SAVE_EVERY_REQUEST = True
# SESSION_COOKIE_AGE = 86400
# SESSION_COOKIE_DOMAIN = None
# SESSION_COOKIE_NAME = 'sessionid'
# SESSION_COOKIE_SECURE = False

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://%s:%s/1" % (REDIS_IP, REDIS_PORT),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "IGNORE_EXCEPTIONS": True,
        }
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

CACHEOPS_DEFAULTS = {
    'timeout': 60 * 60
}
CACHEOPS_REDIS = {
    'host': REDIS_IP,
    'port': REDIS_PORT,
    'db': 2
}
CACHEOPS = {
    'auth.*': {'ops': ('fetch', 'get')},
    'auth.permission': {'ops': 'all'},
    'dlabs_users.*': {'ops': 'all'},
    '*.*': {},
}

CACHEOPS_FAKE = False

SWAGGER_SETTINGS = {
    'exclude_namespaces': [],
    'api_version': '1',
    'api_path': '/',
    'enabled_methods': [
        'get',
        'post',
        'put',
        'patch',
        'delete'
    ],
    'api_key': '',
    'is_authenticated': True,
    'is_superuser': True,
    'permission_denied_handler': None,
    'resource_access_handler': None,
    'info': {
        'contact': 'apiteam@wordnik.com',
        'description': 'This is a sample server Petstore server. '
                       'You can find out more about Swagger at '
                       '<a href="http://swagger.wordnik.com">'
                       'http://swagger.wordnik.com</a> '
                       'or on irc.freenode.net, #swagger. '
                       'For this sample, you can use the api key '
                       '"special-key" to test '
                       'the authorization filters',
        'license': 'Apache 2.0',
        'licenseUrl': 'http://www.apache.org/licenses/LICENSE-2.0.html',
        'termsOfServiceUrl': 'http://helloreverb.com/terms/',
        'title': 'App Documentation',
    },
    'doc_expansion': 'none',
}

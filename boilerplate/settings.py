import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from celery.schedules import crontab

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')5m-kqnx8cds7g&#0tbk4*v^jwhiyfs&@xyw(+628fcpqbe+u@'

ALLOWED_HOSTS = ['*']

# -----------------
# Application definition
# -----------------

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'oauth2_provider',
    'social.apps.django_app.default',
    'corsheaders',
    'tornado_app',
    'common',
]

MIDDLEWARE_CLASSES = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'boilerplate.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'boilerplate.wsgi.application'

# -----------------
# Password validation
# -----------------

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# -----------------
# Internationalization
# -----------------

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# -----------------------
# AUTHENTICATION
# -----------------------


AUTHENTICATION_BACKENDS = (
    # Facebook OAuth2
    'social.backends.facebook.FacebookAppOAuth2',
    'social.backends.facebook.FacebookOAuth2',

    # django-rest-framework-social-oauth2
    'rest_framework_social_oauth2.backends.DjangoOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.social_auth.associate_by_email',
    'auth.pipeline.create_user',
    'social.pipeline.social_auth.associate_user',
)

# -----------------
# CORS
# -----------------

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_REPLACE_HTTPS_REFERER = True
CORS_URLS_REGEX = '^.*$'

CORS_ALLOW_METHODS = (
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS'
)
CORS_ALLOW_HEADERS = (
    'cookie',
    'content-type',
    'content-range',
    'content-length',
    'content-disposition',
    'cache-control',
    'connection',
    'accept',
    'accept-encoding',
    'accept-language',
    'host',
    'origin',
    'referer',
    'authorization',
    'user-agent',
    'x-requested-with',
    'x-csrftoken',
    'x-requested-with',
)

CORS_EXPOSE_HEADERS = ()
CORS_ORIGIN_WHITELIST = ()

# -----------------
# Django Rest Framework
# -----------------

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',
        'rest_framework_social_oauth2.authentication.SocialAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_PAGINATION_CLASS':
        'common.drf.pagination.StandardResultsSetPagination',
    'PAGE_SIZE': 20,
    'MAX_PAGE_SIZE': 300,

    # Authentication
    'UNAUTHENTICATED_USER': 'django.contrib.auth.models.AnonymousUser',
    'UNAUTHENTICATED_TOKEN': None,
}

SWAGGER_SETTINGS = {
    'token_type': 'Bearer',
}

# -----------------
# Static files
# -----------------

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')

# Uncomment it if project uses your own staticfiles

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
# ]

# -----------------------
# Local setting overwrite
# -----------------------

try:
    from local_settings import *
except ImportError:
    pass


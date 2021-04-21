"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

from django.conf.global_settings import CSRF_COOKIE_SECURE, SESSION_COOKIE_SECURE
from environs import Env

env = Env()
env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = env("DJANGO_SECRET_KEY")

"""
with open('./config/secrets.key') as secret_key:
    SECRET_KEY = secret_key.read().strip()
"""

SECRET_KEY = env("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DJANGO_DEBUG", default= False)
#CSRF_COOKIE_SECURE = True
#SESSION_COOKIE_SECURE = True
#SILENCED_SYSTEM_CHECKS=['security.W004']



ALLOWED_HOSTS = ['.herokuapp.com', '127.0.0.1', '0.0.0.0']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'whitenoise.runserver_nostatic',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Error: Site doesn't declare an explicit app_label and isn't in an application in INSTALLED_APPS.
    # https://stackoverflow.com/questions/35388637/runtimeerror-model-class-django-contrib-sites-models-site-doesnt-declare-an-ex
    # FIX
    'django.contrib.sites',

    # Third party
    'crispy_forms',
    'allauth',
    'allauth.account',
    'debug_toolbar',


    # Local
    'accounts',
    'pages',
    'books',
]

MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]
ACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 604800 #(1 Week 60s X 60m X 168h)
CACHE_MIDDLEWARE_KEY_PREFIX = ''
ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath('templates'))],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": env.dj_db_url("DATABASE_URL",
                             default="postgres://postgres@db/postgres")
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (str(BASE_DIR.joinpath('static')),)
STATIC_ROOT = str(BASE_DIR.joinpath('staticfiles'))

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# This will cause our project to use CustomUser instead of the default User model.
AUTH_USER_MODEL = 'accounts.CustomUser'

LOGIN_REDIRECT_URL = 'home'

ACCOUNT_LOGOUT_REDIRECT = 'home'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# django-allauth config
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_AUTHENTICATION_METHOD ="email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
DEFAULT_FROM_EMAIL = 'moh@AbuNayla.com'

SITE_ID = 1
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# django-allauth will send such an email upon a successful user registration, which we can and
# will customize later, but since we don’t yet have a SMTP server properly configured, it will result
# in an error.
# The solution, for now, is to have Django output any emails to the command line console instead.
# Thus we can override the default, implicit config by using console instead of smtp .
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


MEDIA_URL = '/media/'
MEDIA_ROOT = str(BASE_DIR.joinpath('media'))
STATICFILES_STORAGE ='whitenoise.storage.CompressedManifestStaticFilesStorage'

# for debug-toolbar, we need to insure that our internal ips matches that of our Docker host
import socket
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[:-1] + "1" for ip in ips]


SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)
SECURE_HSTS_SECONDS = env.int("DJANGO_SECURE_HSTS_SECONDS", default=2592000)# 1 month
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool("DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True)
SECURE_HSTS_PRELOAD = env.bool("DJANGO_SECURE_HSTS_PRELOAD", default=True)
SESSION_COOKIE_SECURE = env.bool("DJANGO_SESSION_COOKIE_SECURE", default= True)
CSRF_COOKIE_SECURE =env.bool("DJANGO_CSRF_COOKIE_SECURE", default= True)

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
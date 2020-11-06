"""
Django settings for DRF_Boilerplate project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

from dotenv import load_dotenv

load_dotenv()
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "TempSecretKey")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
DEBUG_PROPAGATE_EXCEPTIONS = True

ALLOWED_HOSTS = ['localhost', os.environ.get("PROD_HOSTNAME_1"), os.environ.get("PROD_HOSTNAME_2")]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Rest Framework
    'rest_framework',
    'rest_framework.authtoken',

    # Rest Auth
    'rest_auth',
    'rest_auth.registration',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # * Add your desired social auth providers below
    # 'allauth.socialaccount.providers.google',

    # Other Libraries
    'django_filters',
    'drf_yasg',
    'corsheaders',

    # Apps
    'users_module'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'DRF_Boilerplate.urls'

# If you wish to have a Custom User Model, please go to the users_module app and go through all the files there.
# There are detailed instructions on setting up the same. Uncomment the following line once the setup there is
# complete.

AUTH_USER_MODEL = 'users_module.User'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'DRF_Boilerplate.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


DATABASES = {
    'test': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },

}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'

# REST FRAMEWORK SETTINGS
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        # Set throttling rates here
        'anon': '50/minute',
        'user': '100/minute'
    },
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'

}

# REST AUTH SETTINGS
SITE_ID = 1

REST_AUTH_SERIALIZERS = {
    # 'LOGIN_SERIALIZER': 'users_module.serializers.CustomLoginSerializer'
}

REST_AUTH_REGISTER_SERIALIZERS = {
    # 'REGISTER_SERIALIZER': 'users_module.serializers.CustomRegisterSerializer'
}

# Mandate the need for an Email Address when registering.
ACCOUNT_EMAIL_REQUIRED = True

# Choose whether to use Email or Username to login. Omit to set as 'username'
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'

# Choose if user is logged out after changing password
LOGOUT_ON_PASSWORD_CHANGE = True

# Choose the username field. None if not using username. Omit setting if using the default 'username' field.
# ACCOUNT_USER_MODEL_USERNAME_FIELD = "username"

# Choose whether a username is required during registration. Omit setting if using the default 'username' field.
# ACCOUNT_USERNAME_REQUIRED = False

# Choose whether old password needs to be entered when changing password
OLD_PASSWORD_FIELD_ENABLED = True

# Choose whether email verification is required before login is allowed. Other options are: 'optional' ,
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

# Ensure that the following two settings point to the frontend's Login route. This is to redirect the user after
# successful email confirmations and such.
LOGIN_URL = os.environ.get('LOGIN_URL')
LOGIN_REDIRECT_URL = os.environ.get('LOGIN_REDIRECT_URL')

# CORS SETTINGS
CORS_ORIGIN_ALLOW_ALL = True

# HEROKU Settings

if bool(int(os.environ.get("PROD", "0"))) and bool(int(os.environ.get("HEROKU", "0"))):
    # HEROKU SETTINGS
    import django_heroku

    django_heroku.settings(locals())

    if 'DATABASE_URL' in os.environ:
        import dj_database_url

        DATABASES = {'default': dj_database_url.config()}

# DOCKER Settings

if bool(int(os.environ.get("DOCKER", "0"))):
    DATABASES = {'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }}

# EMAIL SETTINGS
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_HOST_USER = 'no-reply@mail.your-mailgun-registered-subdomain.domain.com'
# EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = "your-mailgun-api-key"
# EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = "no-reply@subdomain.domain.com"
EMAIL_PORT = 465
EMAIL_USE_SSL = True

"""
Django settings for glimcy project.
Generated by 'django-admin startproject' using Django 4.1.4.
For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path
from datetime import timedelta
import json

from django.core.management.utils import get_random_secret_key
from cryptography.fernet import Fernet
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env(env_file=BASE_DIR / '.env')

COLLECTION_FILE_PATH = BASE_DIR / 'nftion/collections.txt'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())
FERNET_SECRET_KEY = Fernet.generate_key()
# APPEND_SLASH = False
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

CSRF_TRUSTED_ORIGINS = [
    "http://*.localhost:*",
    "http://localhost:*",
    "https://stage-api.example.com",
    "https://api.example.com",
    "http://192.168.10.50/",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:8000",
]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

# Application definition
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "corsheaders",
    "rest_framework",
    'rest_framework.authtoken',
    'dj_rest_auth',
    "drf_spectacular",
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'dj_rest_auth.registration',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'django_celery_beat',
]

LOCAL_APPS = [
    "accounts.apps.AccountsConfig",
    "nftion"
]

INSTALLED_APPS = [*DJANGO_APPS, *THIRD_PARTY_APPS, *LOCAL_APPS]

AUTH_USER_MODEL = "accounts.User"

MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "glimcy.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "glimcy.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

PASSWORD_HASHERS = [
    # python -m pip install argon2-cffi
    # https://docs.djangoproject.com/en/3.2/topics/auth/passwords/#using-argon2-with-django
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 92,
    "DEFAULT_AUTHENTICATION_CLASSES": [
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {"anon": "100/hour", "user": "1000/hour"},
    "EXCEPTION_HANDLER": "glimcy.utils.api_exception_handler",
}

REST_AUTH = {
    'USE_JWT': True,
    'JWT_AUTH_COOKIE': 'my-app-auth',
    'JWT_AUTH_REFRESH_COOKIE': 'my-refresh-token',
    'JWT_AUTH_HTTPONLY': False,
}

# Setting for dj-rest-auth
SITE_ID = 2
REST_USE_JWT = True
JWT_AUTH_COOKIE = 'my-app-auth'
AUTHENTICATION_BACKENDS = [
    'allauth.account.auth_backends.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
]

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'none'

DESCRIPTION = f"Django Rest API"

SPECTACULAR_SETTINGS = {
    "TITLE": "Django Rest API",
    "DESCRIPTION": DESCRIPTION,
    "VERSION": "1.0",
    "SERVE_INCLUDE_SCHEMA": False,
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": False,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=1),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}

CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:8080",
    "http://localhost:8000",
    "http://localhost:3000",  # React App will be on this port
    "http://127.0.0.1:9000",
    "http://192.168.10.50:3000",
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_URL = "static/"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "uploads/"
MEDIA_ROOT = BASE_DIR / "uploads"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.zoho.com'
# Push your email
EMAIL_HOST_USER = env('EMAIL_SENDER')
# Push your password
EMAIL_HOST_PASSWORD = env('EMAIL_SENDER_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': env('SOCIAL_AUTH_GOOGLE_CLIENT_ID'),
            'secret': env('SOCIAL_AUTH_GOOGLE_SECRET'),
            'key': ''
        }
    },
    'facebook': {
        'APP': {
            'client_id': env('FB_CLIENT_ID'),
            'secret': env('FB_SECRET'),
            'key': ''
        }
    }
}

# CLOUDINARY
CLOUDINARY_URL = env('CLOUDINARY_URL')

# opensea
API_KEY = env('OPENSEA_api_key')
API_KEY_HISTORICAL = env('OPENSEA_API_KEY_HISTORICAL')

# block_daemon
BLOCK_DAEMON_API_KEY = env('BLOCK_DAEMON_API_KEY')

# celery
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
CELERY_TIMEZONE = "UTC"
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

if DEBUG:

    # stripe
    STRIPE_SECRET_KEY = env('STRIPE_SECRET_KEY')
    STRIPE_API_VERSION = env('STRIPE_API_VERSION')

    # paypal
    PAYPAL_CLIENT_ID = env('PAYPAL_CLIENT_ID')
    PAYPAL_CLIENT_SECRET = env('PAYPAL_CLIENT_SECRET')
    PAYPAL_BASE_URL = env('PAYPAL_BASE_URL')

    # subscription plans
    with open(f'{BASE_DIR}/test_subscription_plans.json', 'r') as f:
        data = json.load(f)

    SUBSCRIPTION_PLANS = data['SUBSCRIPTION_PLANS']

    # CELERY
    CELERY_BROKER_URL = env('REDIS_URL')
    CELERY_RESULT_BACKEND = env('REDIS_URL')

else:
    # stripe
    STRIPE_SECRET_KEY = env('LIVE_STRIPE_SECRET_KEY')
    STRIPE_API_VERSION = env('STRIPE_API_VERSION')

    # paypal
    PAYPAL_CLIENT_ID = env('LIVE_PAYPAL_CLIENT_ID')
    PAYPAL_CLIENT_SECRET = env('LIVE_PAYPAL_CLIENT_SECRET')
    PAYPAL_BASE_URL = env('LIVE_PAYPAL_BASE_URL')

    # subscription plans
    with open(f'{BASE_DIR}/subscription_plans.json', 'r') as f:
        data = json.load(f)

    SUBSCRIPTION_PLANS = data['SUBSCRIPTION_PLANS']

    # CELERY
    CELERY_BROKER_URL = env('LIVE_REDIS_URL')
    CELERY_RESULT_BACKEND = env('LIVE_REDIS_URL')


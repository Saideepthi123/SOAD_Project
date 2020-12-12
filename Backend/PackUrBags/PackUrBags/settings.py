"""
Django settings for PackUrBags project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from datetime import timedelta

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(bl0!sqfyegu$h*(o8fwle4tu-)12joyh2yy_))q5@@gyln@@6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'Tourism',
    'authentication',
    'rest_framework',
    'guide',
    'monuments',
    'rest_framework.authtoken',
]

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=2),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

CORS_ALLOWED_ORIGINS = [
    "https://packurbags.azurewebsites.net",
    "http://127.0.0.1:8000",
    "http://localhost:8000"
]
CSRF_TRUSTED_ORIGINS = [
    '*',
]

if DEBUG is True:
    INSTALLED_APPS += ('corsheaders',)

SITE_ID = 1
SOCIALACCOUNT_QUERY_EMAIL = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'PackUrBags.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'PackUrBags.wsgi.application'
AUTH_USER_MODEL = 'authentication.UserData'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'PackUrBagsDB',
        'CLIENT': {
            'host': 'mongodb+srv://soad:subu@cluster0.rllki.mongodb.net/PackUrBagsDB?retryWrites=true&w=majority',
            'username': 'soad',
            'password': 'subu',
            'authMechanism': 'SCRAM-SHA-1'
        }
    }
}

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

REST_FRAMEWORK = {
    'NON_FIELD_ERRORS_KEY': 'error',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authtoken',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.AllowAny',
    ]
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

CRISPY_TEMPLATE_PACK = 'bootstrap3'
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'tourism.packurbags@gmail.com'
EMAIL_HOST_PASSWORD = 'packurbags@123'
SKYSCANNER_KEY = "5c5035c1e7msh72f101263df16acp1caccdjsna75f7e1a26e5"
SKYSCANNER_HOST = "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"

ZOMATO_API_KEY = "46834a308c05c7cc9b75edf24118a0af"

HOTEL_KEY = "5c5035c1e7msh72f101263df16acp1caccdjsna75f7e1a26e5"
HOTEL_HOST = "hotels4.p.rapidapi.com"

STRIPE_PUBLIC_KEY = os.environ.get("STRIPE_PUBLIC_KEY",
                                   'pk_test_51H5nmkAjnGipPjUd1lx3Vkm1TP2yOObpqO5R7HHfZFUo2pFLaal0V2TDoVqNFfPPrwj5e7f6c9r5liQ51YoGJjuF008QKJzDwq')
STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY",
                                   'sk_test_51H5nmkAjnGipPjUdCXdQBnuUf7r8LJ9V6GS3BF60G8DKD2Y5etEFiNsC1GjhduionCsESqYsROD8Rbo8TmuasK3A00AMvRnaRL')
STRIPE_TEST_SECRET_KEY = 'sk_test_51H5nmkAjnGipPjUdCXdQBnuUf7r8LJ9V6GS3BF60G8DKD2Y5etEFiNsC1GjhduionCsESqYsROD8Rbo8TmuasK3A00AMvRnaRL'
DJSTRIPE_WEBHOOK_VALIDATION = 'retrieve_event'

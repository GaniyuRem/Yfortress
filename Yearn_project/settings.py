<<<<<<< HEAD
"""
Django settings for Yearn_project project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import environ
import django_on_heroku
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
env = environ.Env()
env.read_env(".env")
=======
from pathlib import Path
import os
import django_heroku
import environ
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(SECRET_KEY=str,)
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
>>>>>>> b828d8e30ae34c335fc9150203a66c373a50b557
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
<<<<<<< HEAD
# SECRET_KEY = env.get_value("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!

SECRET_KEY = env.get_value('DJANGO_SECRET_KEY')
ALLOWED_HOSTS = [env.get_value('DJANGO_ALLOWED_HOSTS')]
DEBUG = env.get_value('DJANGO_DEBUG')
=======
SECRET_KEY = env('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DJANGO_DEBUG')

ALLOWED_HOSTS = [env('DJANGO_ALLOWED_HOSTS')]
>>>>>>> b828d8e30ae34c335fc9150203a66c373a50b557


# Application definition

INSTALLED_APPS = [
    'Yearn_finance',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Yearn_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'Yearn_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
<<<<<<< HEAD
# env.get_value("DB_USER_NAME")
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env("DB_NAME"),
        'USER': env("DB_USER_NAME"),
        'PASSWORD': env("DB_PASSWORD"),
    }
}

=======
# DB_USER = 'my_user'
# DB_PWD = 'my_pwd'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'yearn_project',
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PWD'],
    }
}


>>>>>>> b828d8e30ae34c335fc9150203a66c373a50b557
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

<<<<<<< HEAD
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
django_on_heroku.settings(locals())
=======
STATIC_ROOT = os.path.join(BASE_DIR,"staticfiles")
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
print("hello", STATICFILES_DIRS)
django_heroku.settings(locals())
>>>>>>> b828d8e30ae34c335fc9150203a66c373a50b557

"""
Django settings for djangoapp project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-d_=ranv+m#*^#d%p$n=asx212qnled#!^c2os=l*+x4_7*pj*r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True #si es en local debe ser true, pero en deployment debe ser false

ALLOWED_HOSTS = []

#jsjsjs


# Application definition

INSTALLED_APPS = [ #son las apps que se van a instalar, o que están instaladas dentro de la carpeta djangoapp (proyecto)
    'polls.apps.PollsConfig', #app polls
    'django.contrib.admin', #admin, sirve para  administrar el proyecto
    'django.contrib.auth', #auth, sirve para autenticar usuarios
    'django.contrib.contenttypes', #contenttypes, sirve para los tipos de contenido
    'django.contrib.sessions', #sessions, sirve para las sesiones
    'django.contrib.messages', #messages, sirve para los mensajes entre usuarios
    'django.contrib.staticfiles', #staticfiles, sirve para los archivos estáticos, que son los que no cambian, HTML, CSS, JS, etc...
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

ROOT_URLCONF = 'djangoapp.urls'

TEMPLATES = [ #configuración de los templates, que son basicamente html con código de python
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'djangoapp.wsgi.application' #es el archivo que se encarga de ejecutar el proyecto, es el que se ejecuta con el comando python manage.py runserver


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = { #configuración de la base de datos, en este caso es sqlite3, pero puede ser mysql, postgresql, etc...
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        #aqui se pueden añadir user, password, host, etc...
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us' #idioma: inglés

TIME_ZONE = 'UTC' #zona horaria

USE_I18N = True #internacionalización

USE_TZ = True #zona horaria de tiempo, si es true, usa la zona horaria de TIME_ZONE


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/polls/' #url de los archivos estáticos, en este caso es polls, pero puede ser cualquier nombre

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

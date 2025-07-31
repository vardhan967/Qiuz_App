"""
Django settings for Quiz_Base project.

This is a PRODUCTION-READY settings file configured for deployment.
"""

from pathlib import Path
import os
import dj_database_url # For parsing DATABASE_URL environment variable

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# ==============================================================================
# CORE DEPLOYMENT SETTINGS
# ==============================================================================

# ⚠️ SECURITY WARNING: a secret key must be set in your production environment!
# On PythonAnywhere, set this in the "Web" tab, under "Environment variables".
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# ⚠️ SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Set this to the domain name of your live website.
ALLOWED_HOSTS = ['Suvarna.pythonanywhere.com']


# ==============================================================================
# APPLICATION DEFINITION
# ==============================================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # Whitenoise for static files needs to be before contrib.staticfiles
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'Quiz_App', # Your custom app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # Whitenoise Middleware for serving static files efficiently
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Quiz_Base.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'Quiz_App', 'templates', 'Quiz_App')],
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

WSGI_APPLICATION = 'Quiz_Base.wsgi.application'


# ==============================================================================
# DATABASE
# ==============================================================================
# ⚙️ Use a robust database like PostgreSQL or MySQL in production.
# This config reads connection info from a DATABASE_URL environment variable.
# On PythonAnywhere, you would typically configure MySQL and set this variable.

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=False)
}
# Note: For PythonAnywhere's own MySQL, you might need to configure this manually
# if you don't use a DATABASE_URL. See their documentation for details.


# ==============================================================================
# PASSWORD VALIDATION
# ==============================================================================

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ==============================================================================
# INTERNATIONALIZATION
# ==============================================================================

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# ==============================================================================
# STATIC FILES (CSS, JAVASCRIPT, IMAGES)
# ==============================================================================
# 📦 Settings for collecting and serving static files in production.

STATIC_URL = '/static/'
# The directory where `collectstatic` will gather all static files.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Recommended storage backend for Whitenoise.
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# ==============================================================================
# DEFAULT PRIMARY KEY FIELD TYPE
# ==============================================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

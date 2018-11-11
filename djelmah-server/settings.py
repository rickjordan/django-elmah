from decouple import config, Csv
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Security
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', cast=bool)
INTERNAL_IPS = config('INTERNAL_IPS', cast=Csv())
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# Application Definition
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'index'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tastypie',
    'djelmah',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'djelmah.middleware.DjelmahLogMiddleware',
]

ROOT_URLCONF = 'djelmah-server.urls'

TEMPLATES = [
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

WSGI_APPLICATION = 'djelmah-server.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE'),
        'NAME': (
            os.path.join(BASE_DIR, config('DB_NAME'))
            if config('DB_ENGINE').split('.').pop() == 'sqlite3'
            else config('DB_NAME')
        ),
        'USER': config('DB_USER', default=''),
        'PASSWORD': config('DB_PWD', default=''),
        'HOST': config('DB_HOST', default=''),
    }
}

# Password Validation
AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static Files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

if DEBUG:
    INSTALLED_APPS.append('webpack_loader')
    WEBPACK_LOADER = {
        'DEFAULT': {
            'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
        }
    }

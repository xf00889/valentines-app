from .settings import *

DEBUG = True  # Temporarily set to True to see errors

# Updated with your PythonAnywhere username
ALLOWED_HOSTS = ['hutchie.pythonanywhere.com']

# Explicitly include installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'valentines_app',
    'crispy_forms',
    'crispy_bootstrap5',
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hutchie$valentines_db',
        'USER': 'hutchie',
        'PASSWORD': 'valiao#ABCD',
        'HOST': 'hutchie.mysql.pythonanywhere-services.com',
    }
}

# Static files configuration
STATIC_ROOT = '/home/hutchie/valentines-app/static'
STATIC_URL = '/static/'

# Media files configuration
MEDIA_ROOT = '/home/hutchie/valentines-app/media'
MEDIA_URL = '/media/'

# Security settings
SECURE_SSL_REDIRECT = False  # Temporarily disable for debugging
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# HTTPS settings
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True 
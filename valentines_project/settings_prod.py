from .settings import *

DEBUG = False

# Replace yourusername with your PythonAnywhere username
ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'yourusername$valentines_db',
        'USER': 'yourusername',
        'PASSWORD': 'your-database-password',  # Set this in PythonAnywhere's bash console
        'HOST': 'yourusername.mysql.pythonanywhere-services.com',
    }
}

# Static files configuration
STATIC_ROOT = '/home/yourusername/valentines-app/static'
STATIC_URL = '/static/'

# Media files configuration
MEDIA_ROOT = '/home/yourusername/valentines-app/media'
MEDIA_URL = '/media/'

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# HTTPS settings
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True 
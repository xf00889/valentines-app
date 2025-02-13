import os
import sys

# Updated with your PythonAnywhere username
path = '/home/hutchie/valentines-app'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'valentines_project.settings_prod'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application() 
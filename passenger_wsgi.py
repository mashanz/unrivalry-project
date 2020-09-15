from django.core.wsgi import get_wsgi_application
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, f"{BASE_DIR}/unrivalry/core")

os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'

application = get_wsgi_application()

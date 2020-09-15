from django.core.wsgi import get_wsgi_application
import os
import sys

sys.path.insert(0, "/home/unrivalr/django/unrivalry-project/unrivalry")

os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'

application = get_wsgi_application()

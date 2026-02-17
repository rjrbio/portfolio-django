import os
import sys

# Añadir el proyecto al path
sys.path.insert(0, os.path.dirname(__file__))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

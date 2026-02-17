import os
import sys

# Añadir la carpeta del proyecto al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "portfolio"))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

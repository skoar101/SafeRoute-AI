
"""
Purpose: WSGI entrypoint for deployment (production servers)
"""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'saferouteai.settings')
application = get_wsgi_application()

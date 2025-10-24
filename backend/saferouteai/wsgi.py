<<<<<<< HEAD
"""
Purpose: WSGI entrypoint for deployment (production servers)
"""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'saferouteai.settings')
application = get_wsgi_application()
=======
"""
Purpose: WSGI entrypoint for deployment (production servers)
"""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'saferouteai.settings')
application = get_wsgi_application()
>>>>>>> 2f55220dae0bb14c7c90517c68fd70ac27d114b2

"""
WSGI config for ItsList project.
from dotenv import load_dotenv
project_folder = os.path.expanduser('~/your-project-dir')
load_dotenv(os.path.join(project_folder, '.env'))

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ItsList.settings')

application = get_wsgi_application()

"""
WSGI config for roofing project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""
import os,sys

from django.core.wsgi import get_wsgi_application

curr_dir = os.path.dirname(__file__)

sys.path.append(curr_dir)
sys.path.append(os.path.dirname(curr_dir))

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

application = get_wsgi_application()
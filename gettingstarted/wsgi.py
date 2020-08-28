"""
WSGI config for gettingstarted project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gettingstarted.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()


"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "abuse.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

import heroku_bouncer
application = heroku_bouncer.bouncer(application)

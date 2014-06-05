"""
WSGI config for fuse2014 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fuse2014.settings")

_application = None

env_variables_to_pass = ['FUSEDATABASE', 'FUSEUSER', 'FUSEPASSWORD']


def application(environ, start_response):
    for var in env_variables_to_pass:
        os.environ[var] = environ.get(var, '')
    global _application
    if _application is None:
        from django.core.wsgi import get_wsgi_application
        _application = get_wsgi_application()
    return _application(environ, start_response)
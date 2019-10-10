"""
WSGI config for testproj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testproj.settings')

application = get_wsgi_application()

from socketio_app.views import sio
import socketio
# from socketio import Middleware

# application = socketio.WSGIApp(sio, application)

from socketio import Middleware
application = Middleware(sio, application)

import eventlet
import eventlet.wsgi
eventlet.wsgi.server(eventlet.listen(('', 8000)), application)
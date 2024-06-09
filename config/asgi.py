"""
ASGI config for foodapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter, URLRouter

# from channels.security.websocket import AllowedHostsOriginValidator # To use with allowed host origin
from django.core.asgi import get_asgi_application
from django.urls import path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.base")

# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models

asgi_app = get_asgi_application()

from backend.common.consumers import NotificationConsumer
from backend.common.middleware.channel_jwt_auth_middleware import ChannelJwtAuthMiddleware

websocket_urlpatterns = [path("ws/notifications/", NotificationConsumer.as_asgi())]

application = ProtocolTypeRouter(
    {
        "http": asgi_app,
        "websocket": ChannelJwtAuthMiddleware(URLRouter(websocket_urlpatterns)),
    }
)

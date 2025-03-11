# SignMeet/asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from conferencing import consumers  # This is a relative import
from django.urls import path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SignMeet.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path('ws/video-call/<str:room_name>/', consumers.VideoCallConsumer.as_asgi),
        ])
    ),
})
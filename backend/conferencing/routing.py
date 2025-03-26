from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path("ws/sign_detection/", consumers.SignDetectionConsumer.as_asgi()),
]
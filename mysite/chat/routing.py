from django.urls import re_path
from django.core.asgi import get_asgi_application
from . import consumers

websocket_urlpatterns = [
    re_path(r'', consumers.ChatConsumer.as_asgi())
]
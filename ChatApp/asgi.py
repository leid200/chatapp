import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
import chat_main.routing



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ChatApp.settings')

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':AuthMiddlewareStack(URLRouter(chat_main.routing.websocket_urlpatterns)),
})

from channels.routing import ProtocolTypeRouter, URLRouter
from notes import routing
from channels.auth import AuthMiddlewareStack


application = ProtocolTypeRouter(
    {
        'websocket': AuthMiddlewareStack(
            URLRouter(
                routing.websocket_urlpatterns
            )
        )
    }
)
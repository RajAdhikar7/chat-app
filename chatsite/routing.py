# routing.py

# Import necessary modules
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from django.urls import path
from chat import consumers  # Import your consumer

# Define the application routing
application = ProtocolTypeRouter({
    # Define HTTP handling (standard Django)
    "http": get_asgi_application(),

    # Define WebSocket handling
    "websocket": AuthMiddlewareStack(
        URLRouter([
            # Map the WebSocket URL pattern to the consumer
            path("ws/chat/", consumers.ChatConsumer.as_asgi()),
        ])
    ),
})

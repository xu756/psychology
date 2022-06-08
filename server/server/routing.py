from django.urls import path
from chat import views


websocket_urlpatterns=[
    path('ws/app/chat', views.ChatConsumer.as_asgi()),
]


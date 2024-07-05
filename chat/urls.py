from django.urls import path

from .views import (
    home_view,
    room_view,
)

urlpatterns = [
    path('', home_view, name='home'),
    path('room/<int:id>/', room_view, name='room'),
]
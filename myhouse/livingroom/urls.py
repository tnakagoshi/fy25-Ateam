from django.urls import path
from .views import LivingRoomView
urlpatterns = [
    path('', LivingRoomView.as_view(), name='livingroom-home'),
]

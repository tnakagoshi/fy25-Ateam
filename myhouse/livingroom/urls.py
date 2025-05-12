from django.urls import path
from .views import LivingRoomView,SofaView,WindowSideView

urlpatterns = [
    path('', LivingRoomView.as_view(), name='livingroom-home'),
    path('sofa/', SofaView.as_view(), name='sofa-home'),
    path('window/', WindowSideView.as_view(), name='window-side'),
]

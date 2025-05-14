from django.urls import path
from .views import contact_view
from .views import CotactListView

urlpatterns = [
    path('contact/', contact_view, name='contact'),
    path('contact/list', CotactListView.as_view(), name='contact-list'),
]
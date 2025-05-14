from django.urls import path
from .views import hello_world,contact_view
urlpatterns = [
    path('', hello_world),
    path('contact/', contact_view, name='contact'),
]

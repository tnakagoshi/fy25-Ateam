from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class LivingRoomView(TemplateView):
    template_name = 'livingroom/home.html'

class SofaView(TemplateView):
    template_name = 'livingroom/sofa.html'

class WindowSideView(TemplateView):
    template_name = 'livingroom/window_side.html'
    

from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView

class listaPrueb(TemplateView):
    template_name = 'usuarios/prueba.html'
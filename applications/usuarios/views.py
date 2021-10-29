from django.shortcuts import render
from django.views.generic import TemplateView, ListView
# Create your views here.

class PruebaUsuario(TemplateView):

    template_name = 'usuarios/prueba.html'


class ListarUsuarios(ListView):
    template_name = "usuarios/lista-usuarios.html"
    context_object_name = 'ListaUsuarios'
    queryset = ['Maria rodriguez', 'Carlos Paredes']


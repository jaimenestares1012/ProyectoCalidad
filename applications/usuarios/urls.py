
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('prueba/', views.PruebaUsuario.as_view()),
    path('lista-usuarios', views.ListarUsuarios.as_view())
]

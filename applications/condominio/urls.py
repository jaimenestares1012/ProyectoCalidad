from django.contrib import admin
from django.urls import path
from django.contrib.auth import login,logout
from . import views
urlpatterns = [
    path('',views.InicioView.as_view()),
    path('iniciar_sesion', views.InicioSesion.as_view(), name="iniciar_sesion")

]

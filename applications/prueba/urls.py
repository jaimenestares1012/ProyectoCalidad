
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('prueba-terror',views.listaPrueb.as_view()),
]

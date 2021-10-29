
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('applications.condominio.urls')),
    path('usuarios/', include('applications.usuarios.urls')),
    path('prueba/', include('applications.prueba.urls'))
]

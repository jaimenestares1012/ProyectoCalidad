from django.contrib import admin
from .models import Usuario, Pago
# Register your models here.



class UsuariosAdmin(admin.ModelAdmin):
    list_display = (
        'nombres',
        'apellidos',
        'nro_departamento',
    )
    search_fields = ('nombres',)
    list_filter = ('pago',)

admin.site.register(Usuario, UsuariosAdmin)

class PagosAdmin(admin.ModelAdmin):
    list_display = (
        'servicio',
        'monto',
        'mora',
        'monto_total',
    )
    search_fields = ('servicio',)
admin.site.register(Pago, PagosAdmin)
from django.db import models

# Create your models here.
class Pago(models.Model):
    fecha=models.DateTimeField('Fecha')
    monto=models.IntegerField('Monto')
    servicio=models.CharField('servicio', max_length=40)
    mora=models.IntegerField('Mora')
    monto_total=models.IntegerField('Monto Total')
    class Meta:
        verbose_name= 'Pago'
        verbose_name_plural= 'Pagos'
        ordering=['fecha']
    def __str__(self):
        return   self.servicio


class Usuario(models.Model):
    nombres=models.CharField('Nombres', max_length=50)
    apellidos=models.CharField('Apellidos', max_length=60)
    nro_departamento=models.IntegerField('N° departamento')
    correo=models.EmailField('Correo')
    celular=models.IntegerField('Celular', max_length=9)
    pago=models.ManyToManyField(Pago)

    class Meta:
        verbose_name= 'Usuario'
        verbose_name_plural= 'Usuarios'
        ordering=['apellidos']

    def __str__(self):
        return str(self.id) + '-' + self.nombres + '-' + self.apellidos
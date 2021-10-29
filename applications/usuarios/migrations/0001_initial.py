# Generated by Django 3.2.8 on 2021-10-24 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(verbose_name='Fecha')),
                ('monto', models.IntegerField(verbose_name='Monto')),
                ('mora', models.IntegerField(verbose_name='Mora')),
                ('monto_total', models.IntegerField(verbose_name='Monto Total')),
            ],
            options={
                'verbose_name': 'Pago',
                'verbose_name_plural': 'Pagos',
                'ordering': ['fecha'],
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=60, verbose_name='Apellidos')),
                ('nro_departamento', models.IntegerField(verbose_name='N° departamento')),
                ('correo', models.EmailField(max_length=254, verbose_name='Correo')),
                ('celular', models.IntegerField(verbose_name='Celular')),
                ('pago', models.ManyToManyField(to='usuarios.Pago')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'ordering': ['apellidos'],
            },
        ),
    ]

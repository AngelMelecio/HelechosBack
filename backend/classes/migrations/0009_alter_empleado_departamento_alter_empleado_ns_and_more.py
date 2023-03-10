# Generated by Django 4.1.4 on 2023-01-01 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0008_alter_empleado_contrasena_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='departamento',
            field=models.CharField(choices=[('Tejido', 'Tejido'), ('Corte', 'Corte'), ('Plancha', 'Plancha'), ('Empaque', 'Empaque'), ('Transporte', 'Transporte'), ('Diseno', 'Diseño'), ('Gerencia', 'Gerencia')], default='Tejido', max_length=20),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='ns',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='tipo',
            field=models.CharField(choices=[('Trabajador', 'Trabajador'), ('Encargado', 'Encargado'), ('Administrador', 'Administrador')], default='Trabajador', max_length=20),
        ),
    ]

# Generated by Django 4.1.4 on 2023-01-01 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0009_alter_empleado_departamento_alter_empleado_ns_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maquina',
            name='departamento',
            field=models.CharField(choices=[('Tejido', 'Tejido'), ('Corte', 'Corte'), ('Plancha', 'Plancha'), ('Empaque', 'Empaque'), ('Transporte', 'Transporte'), ('Diseno', 'Diseño'), ('Gerencia', 'Gerencia')], default='Tejido', max_length=20),
        ),
    ]
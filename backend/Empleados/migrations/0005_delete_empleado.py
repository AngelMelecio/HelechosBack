# Generated by Django 4.1.4 on 2022-12-25 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Empleados', '0004_rename_id_empleado_idempleado'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Empleado',
        ),
    ]

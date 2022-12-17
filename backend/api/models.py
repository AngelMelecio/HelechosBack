from django.db import models


# Create your models here.
class Empleado(models.Model):
    idEmpleado=models.CharField(max_length=20)
    nombre=models.CharField(max_length=200)
    apellidos=models.CharField(max_length=200)
    direccion=models.CharField(max_length=200)
    telefono=models.CharField(max_length=20)
    correo=models.CharField(max_length=200)
    ns=models.CharField(max_length=200)
    usuario=models.CharField(max_length=200)
    contrasena=models.CharField(max_length=200, default='1234')
    fotografia=models.CharField(max_length=255)
    departamento=models.CharField(max_length=200)
    tipo=models.CharField(max_length=200)
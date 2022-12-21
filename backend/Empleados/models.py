from django.db import models


# Create your models here.
class Empleado(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True)
    nombre=models.CharField(max_length=200 )
    apellidos=models.CharField(max_length=200 )
    direccion=models.CharField(max_length=200 )
    telefono=models.CharField(max_length=20 )
    correo=models.CharField(max_length=200, null=True, blank=True)
    ns=models.CharField(max_length=200 )
    usuario=models.CharField(max_length=200 )
    contrasena=models.CharField(max_length=200 )
    fotografia=models.CharField(max_length=255, null=True, blank=True)
    departamento=models.CharField(max_length=200 )
    tipo=models.CharField(max_length=200 )  


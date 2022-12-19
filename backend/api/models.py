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
    permisos=models.CharField(max_length=200)

class Maquina(models.Model):
    idMaquina=models.CharField(max_length=20)
    numero=models.CharField(max_length=50)
    linea=models.CharField(max_length=4)
    marca=models.CharField(max_length=60)
    ns=models.CharField(max_length=60)
    fechaAdquisicion=models.DateField()
    otros=models.CharField(max_length=200)
    departamento=models.CharField(max_length=20)

class Cliente(models.Model):
    idCliente=models.CharField(max_length=20)
    nombre=models.CharField(max_length=200)
    direccion=models.CharField(max_length=200)
    telefono=models.CharField(max_length=20)
    correo=models.CharField(max_length=200)
    otro=models.DateField()
    fotografia=models.CharField(max_length=225)

class Contacto(models.Model):
    idContacto=models.CharField(max_length=20)
    nombre=models.CharField(max_length=200)
    puesto=models.CharField(max_length=200)
    correo=models.CharField(max_length=200)
    telefono=models.CharField(max_length=20)
    idCliente=models.CharField(max_length=20)

class Modelo(models.Model):
    idModelo=models.CharField(max_length=20)
    nombre=models.CharField(max_length=200)
    colores=models.CharField(max_length=200)
    fichaTecnica=models.CharField(max_length=225)

class DetallePedido(models.Model):
    idDetallePedido=models.CharField(max_length=20)
    idPedido=models.CharField(max_length=20)
    talla=models.CharField(max_length=50)
    cantidad=models.CharField(max_length=50)

class Pedido(models.Model):
    idPedido=models.CharField(max_length=20)
    idCliente=models.CharField(max_length=20)
    idModelo=models.CharField(max_length=20)
    fechaActual=models.DateTimeField()
    fechaEntrega=models.DateTimeField()
    proveedores=models.CharField(max_length=200)

class Reposicion(models.Model):
    idReposicion=models.CharField(max_length=20)
    fecha=models.DateTimeField()
    idPedido=models.CharField(max_length=20)
    idEmpleado=models.CharField(max_length=20)
    idMaquina=models.CharField(max_length=20)
    idEmpleadoRepuso=models.CharField(max_length=20)
    idEmpleadoRevisor=models.CharField(max_length=20)
    cantidad=models.CharField(max_length=50)

class EmpleadoMaquina(models.Model):
    idEmpleado=models.CharField(max_length=20)
    idMaquina=models.CharField(max_length=20)

class Produccion(models.Model):
    idProduccion=models.CharField(max_length=20)
    idPedido=models.CharField(max_length=20)
    idDetallePedido=models.CharField(max_length=20)
    idEtiqueta=models.CharField(max_length=20)
    tejido=models.BooleanField()
    fechaTejido=models.DateTimeField()
    idEmpleadoTejedor=models.CharField(max_length=20)
    idMaquinaTejido=models.CharField(max_length=20)
    plancha=models.BooleanField()
    fechaPlancha=models.DateTimeField()
    idEmpleadoPlanchador=models.CharField(max_length=20)
    idMaquinaPlancha=models.CharField(max_length=20)
    corte=models.BooleanField()
    fechaCorte=models.DateTimeField()
    idEmpleadoCortador=models.CharField(max_length=20)
    idMaquinaCorte=models.CharField(max_length=20)
    empaque=models.BooleanField()
    fechaEmpaque=models.DateTimeField()
    idEmpleadoEmpacador=models.CharField(max_length=20)
    salida=models.BooleanField()
    fechaSalida=models.DateTimeField()
    idEmpleadoRepartidor=models.CharField(max_length=20)
    numSemana=models.CharField(max_length=20)
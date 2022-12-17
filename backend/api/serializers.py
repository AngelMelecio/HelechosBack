from rest_framework import serializers
 
# import the todo data model
from .models import Empleado
 
# create a serializer class
class EmpleadoSerializers(serializers.ModelSerializer):
 
    # create a meta class
    class Meta:
        model = Empleado
        fields = (
            "idEmpleado",
            "nombre",
            "apellidos",
            "direccion",
            "telefono",
            "correo",
            "ns",
            "usuario",
            "contrasena",
            "fotografia",
            "departamento",
            "tipo"
        )
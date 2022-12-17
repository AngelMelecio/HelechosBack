from django.contrib import admin

# Register your models here.
from .models import Empleado

class EmpleadoAdmin(admin.ModelAdmin):

    list_display = (
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

admin.site.register(Empleado,EmpleadoAdmin)
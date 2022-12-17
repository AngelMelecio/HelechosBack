from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EmpleadoSerializers
from .models import Empleado

# Create your views here.
class EmpleadoView(viewsets.ModelViewSet):
    serializer_class = EmpleadoSerializers
    queryset = Empleado.objects.all()
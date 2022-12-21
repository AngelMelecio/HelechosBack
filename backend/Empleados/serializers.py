from rest_framework import serializers
 
# import the todo data model
from .models import Empleado
 
# create a serializer class
class EmpleadoSerializer(serializers.ModelSerializer):
 
    # create a meta class
    class Meta:
        model = Empleado
        fields = '__all__'
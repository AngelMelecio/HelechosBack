from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from Empleados.models import Empleado
from Empleados.serializers import EmpleadoSerializer

@api_view(['GET','POST'])
def empleado_api_view(request):

    # list
    if request.method == 'GET':
        empleados = Empleado.objects.all()
        empleados_serializer = EmpleadoSerializer(empleados,many=True)
        return Response( empleados_serializer.data, status=status.HTTP_200_OK )

    # Create
    elif request.method == 'POST':
        empleado_serializer = EmpleadoSerializer(data=request.data)
        if empleado_serializer.is_valid():
            empleado_serializer.save()
            return Response( {'message':'Empleado creado correctamente!.'}, status=status.HTTP_201_CREATED )
        return Response( empleado_serializer.errors, status=status.HTTP_400_BAD_REQUEST )

@api_view(['GET','PUT','DELETE'])
def empleado_detail_api_view(request, pk=None):
    # Queryset
    empleado = Empleado.objects.filter( id = pk ).first()
    
    # Validacion
    if empleado:

        # Retrieve
        if request.method == 'GET':
            empleado_serializer =  EmpleadoSerializer(empleado)
            return Response( empleado_serializer.data, status=status.HTTP_200_OK )
        
        # Update
        elif request.method == 'PUT':
            empleado_serializer = EmpleadoSerializer(empleado, data = request.data)
            if empleado_serializer.is_valid():
                empleado_serializer.save()
                return Response(empleado_serializer.data, status=status.HTTP_200_OK)
            return Response(empleado_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        # Delete
        elif request.method == 'DELETE':
            empleado = Empleado.objects.filter( id = pk ).first()
            empleado.delete()
            return Response(
                {'message':'Empleado eliminado correctamente!.'}, 
                status=status.HTTP_200_OK
            )
    return Response(
        {'message':'No se encontró el empleado...'}, 
        status=status.HTTP_400_BAD_REQUEST
    )
        
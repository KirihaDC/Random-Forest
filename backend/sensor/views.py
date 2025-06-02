from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from .serializers import SensorDataSerializer
from rest_framework.decorators import api_view
from .models import SensorData
from django.views.decorators.csrf import csrf_exempt
import json

class SensorDataView(APIView):
    def post(self, request):
        serializer = SensorDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Data received"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['POST'])
def sensor_data_upload(request):
    serializer = SensorDataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status': 'success'})
    return Response(serializer.errors, status=400)

@csrf_exempt
def recibir_datos_sensor(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            x = data['x']
            y = data['y']
            z = data['z']
            SensorData.objects.create(x=x, y=y, z=z)
            return JsonResponse({'status': 'ok', 'message': 'Datos guardados'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    else:
        return JsonResponse({'status': 'error', 'message': 'Solo POST permitido'})
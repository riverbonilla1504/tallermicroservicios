from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tarea
from .serializers import TareaSerializer

class TareasAPIView(APIView):
    def get(self, request):
        tareas = Tarea.objects.all()
        serializer = TareaSerializer(tareas, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = TareaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class TareasUsuarioAPIView(APIView):
    def get(self, request, id_usuario):
        tareas = Tarea.objects.filter(id_usuario=id_usuario)
        serializer = TareaSerializer(tareas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class TareasCompleteView(APIView):
    def post(self, request, id_tarea):
        tarea = Tarea.objects.get(id=id_tarea)
        tarea.completada = True
        tarea.save()
        return Response(status=status.HTTP_200_OK)
    
class TareasDeleteView(APIView):
    def delete(self, request, id_tarea):
        Tarea.objects.get(id=id_tarea).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
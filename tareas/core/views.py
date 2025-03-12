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
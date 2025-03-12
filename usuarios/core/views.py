from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password, check_password
from .models import usuario
import requests

TAREAS_SERVICE_URL = "http://localhost:8000/api/tareas/"  # Ajusta la URL del servicio de tareas

class RegistroAPIView(APIView):
    def post(self, request):
        data = request.data
        nombre = data.get("nombre")
        email = data.get("email")
        contrasena = data.get("contrasena")

        if usuario.objects.filter(email=email).exists():
            return Response({"error": "El email ya está registrado"}, status=status.HTTP_400_BAD_REQUEST)

        nuevo_usuario = usuario.objects.create(
            nombre=nombre,
            email=email,
            contrasena=make_password(contrasena)  
        )

        return Response({"mensaje": "Usuario registrado correctamente", "id": nuevo_usuario.id}, status=status.HTTP_201_CREATED)

class LoginAPIView(APIView):
    def post(self, request):
        data = request.data
        email = data.get("email")
        contrasena = data.get("contrasena")

        try:
            usuario_obj = usuario.objects.get(email=email)
        except usuario.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        if not check_password(contrasena, usuario_obj.contrasena):
            return Response({"error": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)

        tareas_response = requests.get(f"{TAREAS_SERVICE_URL}{usuario_obj.id}")
        tareas = tareas_response.json() if tareas_response.status_code == 200 else []

        return Response({
            "id": usuario_obj.id,
            "nombre": usuario_obj.nombre,
            "email": usuario_obj.email,
            "tareas": tareas
        }, status=status.HTTP_200_OK)
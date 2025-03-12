from django.urls import path
from .views import TareasAPIView, TareasUsuarioAPIView

urlpatterns = [
    path('tareas', TareasAPIView.as_view()),
    path("tareas/<int:id_usuario>", TareasUsuarioAPIView.as_view(), name="tareas-usuario")
]

from django.urls import path
from .views import TareasAPIView, TareasUsuarioAPIView, TareasCompleteView, TareasDeleteView

urlpatterns = [
    path('tareas', TareasAPIView.as_view()),
    path("tareas/<int:id_usuario>", TareasUsuarioAPIView.as_view(), name="tareas-usuario"),
    path("tareas/completar/<int:id_tarea>", TareasCompleteView.as_view(), name="tareas-completar"),
    path("tareas/eliminar/<int:id_tarea>", TareasDeleteView.as_view(), name="tareas-eliminar")
]

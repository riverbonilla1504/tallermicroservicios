from django.utils import timezone
from django.db import models

class Tarea(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha_recordatorio = models.DateField(default=timezone.now())
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    completada = models.BooleanField(default=False)
    id_usuario = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.nombre
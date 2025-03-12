from django.db import models

class usuario(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    contrasena = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.nombre

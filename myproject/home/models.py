from django.db import models
from django.contrib.auth.models import User

class Tarea(models.Model):
    nombre_tarea = models.CharField(max_length=200)
    descripcion_tarea = models.TextField()
    completar_tarea = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_tarea

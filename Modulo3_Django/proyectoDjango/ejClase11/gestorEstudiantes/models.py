from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField(max_length=3)
    nota = models.IntegerField(max_length=3)
    
    def __str__(self):
        return self.nombre
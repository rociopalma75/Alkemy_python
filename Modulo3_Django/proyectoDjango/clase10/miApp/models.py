from django.db import models

# Create your models here.
class Usuario(models.Model):
    #CAMPOS (NO ATRIBUTOS)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField(max_length=3)


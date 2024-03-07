from django.db import models

# Create your models here.
class Usuario(models.Model):
    
    #CAMPOS
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    esAdmin = models.BooleanField(default=False)
    correo = models.CharField(max_length=150)

    #METADATOS
    class Meta:
        ordering = ['-edad'] #Orden desc en edad

    #METODOS
    def __str__(self): #Mostrar en pantalla un str cuando llamamos el modelo
        return self.name 

from django.shortcuts import render
from .models import Usuario 

# Create your views here.

#Crea instancias de usuario - CREA USUARIO
def crear_usuario(request):
    #hard coding - ingresar datos estaticamente
    nombre = "Valeria"
    edad = 23
    esAdmin = False
    correo = "Valeria@gmail.com"
    usuario = Usuario.objects.create(
        nombre = nombre,
        edad = edad,
        esAdmin = esAdmin,
        correo = correo
    )

    return render(request, 'usuarios.html', {'usuarios' : usuario})

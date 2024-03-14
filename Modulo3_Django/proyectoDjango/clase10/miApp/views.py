from django.shortcuts import render
from .models import Usuario

# Create your views here.
#FUNCIONES
# CRUD -> CREATE . READ . UPDATE . DELETE
# Aplicamos ORM para definir esas funciones

def crearUsuario(request, nombre, apellido, edad):
    nuevo_usuario = Usuario.objects.create(
        nombre = nombre,
        apellido = apellido,
        edad = edad
    )
    return render(request, 'nuevo_usuario.html', {'nuevo_usuario': nuevo_usuario}) # 3er parametro -> html  --- django

def mostrar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'mostrar_usuarios.html', {'usuarios': usuarios})

def filtar_usuarios_edad(request, edad):
    usuariosFiltrados = Usuario.objects.filter(edad = edad)
    return render(request, 'usuarios_filtrados.html', {'usuariosFiltrados': usuariosFiltrados})

def update_usuario_id(request, id, nombre, apellido, edad):
    usuario = Usuario.objects.get(id=id) #Obtiene el usuario
    #Hace los cambios
    usuario.nombre = nombre
    usuario.apellido = apellido
    usuario.edad = edad
    usuario.save() #Guarda los cambios
    usuarios = Usuario.objects.all()
    return render(request, 'mostrar_usuarios.html', {'usuarios': usuarios})

def delete_usuario_id(request, id):
    usuario = Usuario.objects.get(id=id) #Obtiene el usuario
    usuario.delete()
    usuarios = Usuario.objects.all()
    return render(request, 'mostrar_usuarios.html', {'usuarios': usuarios})

def delete_all(request):
    usuarios= Usuario.objects.all()
    usuarios.all()
    return render(request, 'mostrar_usuarios.html', {'usuarios': usuarios})

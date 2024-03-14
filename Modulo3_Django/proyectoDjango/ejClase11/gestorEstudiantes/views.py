from django.shortcuts import render
from .models import Estudiante

# Create your views here.

# Create your views here.
def createEstudiante(request, nombre, apellido, edad, nota):
    nuevoEstudiante = Estudiante.objects.create(
        nombre = nombre,
        apellido = apellido,
        edad = edad,
        nota = nota
    )
    return render(request, 'nuevo_estudiante.html', {'estudiante': nuevoEstudiante})

def readEstudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'lista_estudiantes.html', {'estudiantes' : estudiantes})

def updateNota(request, id, nota):
    estudiante = Estudiante.objects.get(id = id)
    estudiante.nota = nota
    estudiante.save()
    estudiantes = Estudiante.objects.all()
    return render(request, 'lista_estudiantes.html', {'estudiantes': estudiantes})

def filterEstudiante(request, edad):
    estudiantes = Estudiante.objects.filter(edad__gte = edad)
    return render(request, 'lista_estudiantes.html',{'estudiantes':estudiantes})

def deleteEstudiante(request, id):
    estudiante = Estudiante.objects.get(id = id)
    estudiante.delete()
    estudiantes = Estudiante.objects.all()
    return render(request, 'lista_estudiantes.html', {'estudiantes': estudiantes})
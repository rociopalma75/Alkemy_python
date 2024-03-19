from django.shortcuts import render
from django.http import HttpResponse
from .models import Estudiante
from django.template import Template, Context
# Create your views here.

# Create your views here.
def createEstudiante(request, nombre, apellido, edad, nota):
    nuevoEstudiante = Estudiante.objects.create(
        nombre = nombre,
        apellido = apellido,
        edad = edad,
        nota = nota
    )
    ruta = "C:\\Users\\rocio\\OneDrive\\Documentos\\Alkemy_python\\Modulo3_Django\\proyectoDjango\\ejClase11\\gestorEstudiantes\\templates\\nuevo_estudiante.html"
    doc_externo = open(ruta)
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context({"estudiante": nuevoEstudiante})
    return HttpResponse(plantilla.render(contexto))

def readEstudiantes(request):
    estudiantes = Estudiante.objects.all()
    ruta = "C:\\Users\\rocio\\OneDrive\\Documentos\\Alkemy_python\\Modulo3_Django\\proyectoDjango\\ejClase11\\gestorEstudiantes\\templates\\lista_estudiantes.html"
    doc_externo = open(ruta)
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context({"estudiantes":estudiantes})
    return HttpResponse(plantilla.render(contexto))

def updateNota(request, id, nota):
    estudiante = Estudiante.objects.get(id = id)
    estudiante.nota = nota
    estudiante.save()
    estudiantes = Estudiante.objects.all()
    ruta = "C:\\Users\\rocio\\OneDrive\\Documentos\\Alkemy_python\\Modulo3_Django\\proyectoDjango\\ejClase11\\gestorEstudiantes\\templates\\lista_estudiantes.html"
    doc_externo = open(ruta)
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context({"estudiantes":estudiantes})
    return HttpResponse(plantilla.render(contexto))

def filterEstudiante(request, edad):
    estudiantes = Estudiante.objects.filter(edad__gte = edad)
    ruta = "C:\\Users\\rocio\\OneDrive\\Documentos\\Alkemy_python\\Modulo3_Django\\proyectoDjango\\ejClase11\\gestorEstudiantes\\templates\\lista_estudiantes.html"
    doc_externo = open(ruta)
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context({"estudiantes":estudiantes})
    return HttpResponse(plantilla.render(contexto))

def deleteEstudiante(request, id):
    estudiante = Estudiante.objects.get(id = id)
    estudiante.delete()
    estudiantes = Estudiante.objects.all()
    ruta = "C:\\Users\\rocio\\OneDrive\\Documentos\\Alkemy_python\\Modulo3_Django\\proyectoDjango\\ejClase11\\gestorEstudiantes\\templates\\lista_estudiantes.html"
    doc_externo = open(ruta)
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context({"estudiantes":estudiantes})
    return HttpResponse(plantilla.render(contexto))
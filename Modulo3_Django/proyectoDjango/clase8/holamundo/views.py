from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def saludo(request): #Por defecto siempre recibir request
    return HttpResponse("Hola mundo desde django")


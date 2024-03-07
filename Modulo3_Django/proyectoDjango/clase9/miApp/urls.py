from django.urls import path
from .views import crear_usuario #Incluimos la funcion crear_usuario del view

urlpatterns = [
    path('', crear_usuario)
]


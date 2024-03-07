from django.urls import path
from . import views #Importa todo lo que tenga en views

urlpatterns = [
    path('saludo/', views.saludo, name = "saludo")
]

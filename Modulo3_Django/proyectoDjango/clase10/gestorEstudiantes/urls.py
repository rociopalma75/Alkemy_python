from django.urls import path
from . import views

urlpatterns=[
    path('createEstudiante/<str:nombre>/<str:apellido>/<int:edad>/<int:nota>', views.createEstudiante, name="Crear un nuevo estudiante"),
    path('estudiantes', views.readEstudiantes, name = "Mostrar todos los estudiantes"),
    path('updateNota/<int:id>/<int:nota>', views.updateNota, name="Actualizar nota de un estudiante por id"),
    path('filterEstudiantes/<int:edad>', views.filterEstudiante, name="Filtrar estudiantes por edad"),
    path('deleteEstudiante/<int:id>', views.deleteEstudiante, name="Eliminar estudiante por id"),
]
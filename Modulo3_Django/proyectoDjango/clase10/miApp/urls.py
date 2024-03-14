from django.urls import path
from . import views

urlpatterns =[
    path('', views.mostrar_usuarios, name="Mostrar usuarios"), 
    path('create/<str:nombre>/<str:apellido>/<int:edad>', views.crearUsuario, name="Crear usuario"),
    path('filter/<int:edad>', views.filtar_usuarios_edad, name = "Filtrar usuarios por edad"),
    path('update/<int:id>/<str:nombre>/<str:apellido>/<int:edad>', views.update_usuario_id, name="Actualizar usuario por id"),
    path('delete/<int:id>', views.delete_usuario_id, name="borrar usuario por id"),
    path('delete', views.delete_all, name="Borrar todos los usuarios")
]   
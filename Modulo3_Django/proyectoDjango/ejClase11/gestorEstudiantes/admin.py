from django.contrib import admin
from .models import Estudiante

# Register your models here.
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'edad','nota']
    search_fields = ['apellido', 'nota']

admin.site.register(Estudiante, EstudianteAdmin)

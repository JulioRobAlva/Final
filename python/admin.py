from django.contrib import admin
from python.models import Alumno, AlumnoAdmin, Materia, MateriaAdmin
admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Materia, MateriaAdmin)
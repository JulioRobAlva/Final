from django.db import models
from django.contrib import admin

class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    def __str__(self):
        return self.nombre

class TipoMateria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Materia(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    fecha = models.DateField()
    tipo = models.ForeignKey(TipoMateria, on_delete=models.CASCADE,blank=True, null=True)
    alumnos   = models.ManyToManyField(Alumno, through='Inscripcion')
    def __str__(self):
        return self.nombre

class Inscripcion(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

class InscripcionInLine(admin.TabularInline):
    model = Inscripcion
    extra = 1

class AlumnoAdmin(admin.ModelAdmin):
    inlines = (InscripcionInLine,)
    
class MateriaAdmin (admin.ModelAdmin):
    inlines = (InscripcionInLine,)

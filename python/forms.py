from django import forms
from .models import Alumno, Materia, TipoMateria

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ('nombre', 'descripcion', 'fecha', 'alumnos', 'tipo')
        def __init__ (self, *args, **kwargs):
            super(MateriaForm, self).__init__(*args, **kwargs)
            self.fields["alumnos"].widget = forms.widgets.CheckboxSelectMultiple()
            self.fields["alumnos"].help_text = "Alumno"
            self.fields["alumnos"].queryset = Persona.objects.all()

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ('nombre', 'telefono', 'direccion','correo','fecha_nacimiento')

class TipoForm(forms.ModelForm):
    class Meta:
        model=TipoMateria
        fields=('nombre', 'descripcion')

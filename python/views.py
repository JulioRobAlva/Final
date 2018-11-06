from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages
from .forms import MateriaForm, AlumnoForm, TipoForm
from python.models import Materia, Alumno, TipoMateria, Inscripcion
from django.urls import reverse
from django.contrib.auth.decorators import login_required

#MATERIA
def lista_materias(request):
    materias = Materia.objects.filter(fecha__lte=timezone.now()).order_by('fecha')
    return render(request, 'materias/materia_list.html', {'materias':materias})

@login_required
def materia_detalle(request, pk):
    materia = get_object_or_404(Materia, pk=pk)
    return render(request, 'materias/materia_detalle.html', {'materia': materia})

@login_required
def materia_editar(request, pk):
    materia = get_object_or_404(Materia, pk=pk)
    if request.method == "POST":
        form = MateriaForm(request.POST, instance=materia)
        if form.is_valid():
            materia = form.save(commit=False)
            materia.save()
            return redirect('lista_materias')
    else:
        form = MateriaForm(instance=materia)
    return render(request, 'materias/materia_editar.html', {'form': form})

@login_required
def materia_eliminar(request, pk):
    materia = get_object_or_404(Materia, pk=pk)
    materia.delete()
    return redirect('lista_materias')

@login_required
def materia_nuevo(request):
    if request.method == "POST":
        formulario = MateriaForm(request.POST)
        if formulario.is_valid():
            materia = Materia.objects.create(nombre=formulario.cleaned_data['nombre'], descripcion=formulario.cleaned_data['descripcion'], fecha=formulario.cleaned_data['fecha'], tipo=formulario.cleaned_data['tipo'])
            for alumno_id in request.POST.getlist('personas'):
                inscripcion = Inscripcion(alumno_id=alumno_id, materia_id = materia_id.id)
                inscripcion.save()
            messages.add_message(request, messages.SUCCESS, 'Guardado!')
    else:
        formulario = MateriaForm()
    return render(request, 'materias/materia_nuevo.html', {'formulario': formulario})

#ALUMNO
@login_required
def lista_alumnos(request):
    alumnos = Alumno.objects.order_by('id')
    return render(request, 'alumno/alumno_list.html', {'alumnos':alumnos})

@login_required
def alumno_nuevo(request):
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            alumno = form.save(commit=False)
            alumno.save()
            return redirect('lista_alumnos')
    else:
        form = AlumnoForm()
    return render(request, 'alumno/alumno_nuevo.html', {'form': form})

@login_required
def alumno_detalle(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    return render(request, 'alumnos/alumno_detalle.html', {'alumno': alumno})

@login_required
def alumno_editar(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == "POST":
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            alumno = form.save(commit=False)
            alumno.save()
            return redirect('lista_alumnos')
    else:
        form = AlumnoForm(instance=alumno)
    return render(request, 'alumnos/alumno_editar.html', {'form': form})

@login_required
def alumno_eliminar(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    alumno.delete()
    return redirect('lista_alumnos')


#TIPO
@login_required
def lista_tipo(request):
    tipos = TipoMateria.objects.order_by('id')
    return render(request, 'tipos/tipo_list.html', {'tipos':tipos})

@login_required
def tipo_nuevo(request):
    if request.method == "POST":
        form = TipoForm(request.POST)
        if form.is_valid():
            tipo = form.save(commit=False)
            tipo.save()
            return redirect('lista_tipo')
    else:
        form = TipoForm()
    return render(request, 'tipos/tipo_nuevo.html', {'form': form})

@login_required
def tipo_detalle(request, pk):
    tipo = get_object_or_404(TipoMateria, pk=pk)
    return render(request, 'tipos/tipo_detalle.html', {'tipo': tipo})

@login_required
def tipo_editar(request, pk):
    tipo = get_object_or_404(TipoMateria, pk=pk)
    if request.method == "POST":
        form = TipoForm(request.POST, instance=tipo)
        if form.is_valid():
            tipo = form.save(commit=False)
            tipo.save()
            return redirect('lista_tipo')
    else:
        form = TipoForm(instance=tipo)
    return render(request, 'tipos/tipo_editar.html', {'form': form})

@login_required
def tipo_eliminar(request, pk):
    tipo = get_object_or_404(TipoMateria, pk=pk)
    tipo.delete()
    return redirect('lista_tipo')

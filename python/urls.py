from django.conf.urls import include, url
from . import views
urlpatterns = [

    url(r'^$', views.lista_materias, name ='lista_materias'),
    url(r'^materia/(?P<pk>[0-9]+)/$', views.materia_detalle, name='materia_detalle'),
    url(r'^materia/nuevo/$', views.materia_nuevo, name='materia_nuevo'),
    url(r'^materia/(?P<pk>[0-9]+)/edit/$', views.materia_editar, name='materia_editar'),
    url(r'^materia/(?P<pk>\d+)/remove/$', views.materia_eliminar, name='materia_eliminar'),

    url(r'^alumno/$', views.lista_alumnos, name ='lista_alumnos'),
    url(r'^alumno/nueva/$', views.alumno_nuevo, name='alumno_nuevo'),
    url(r'^alumno/(?P<pk>[0-9]+)/$', views.alumno_detalle, name='alumno_detalle'),
    url(r'^alumno/(?P<pk>[0-9]+)/edit/$', views.alumno_editar, name='alumno_editar'),
    url(r'^alumno/(?P<pk>\d+)/remove/$', views.alumno_eliminar, name='alumno_eliminar'),

    url(r'^tipoMateria/$', views.lista_tipo, name ='lista_tipo'),
    url(r'^tipoMateria/nuevo/$', views.tipo_nuevo, name='tipo_nuevo'),
    url(r'^tipoMateria/(?P<pk>[0-9]+)/$', views.tipo_detalle, name='tipo_detalle'),
    url(r'^tipoMateria/(?P<pk>[0-9]+)/edit/$', views.tipo_editar, name='tipo_editar'),
    url(r'^tipoMateria/(?P<pk>\d+)/remove/$', views.tipo_eliminar, name='tipo_eliminar'),

]

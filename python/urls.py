from django.conf.urls import include, url
from . import views
urlpatterns = [

    url(r'^$', views.lista_materias, name ='lista_materias'),
    #url(r'^$', views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    url(r'^grado/(?P<pk>[0-9]+)/$', views.materia_detalle, name='materia_detalle'),
    url(r'^grado/nuevo/$', views.materia_nuevo, name='materia_nuevo'),
    url(r'^grado/(?P<pk>[0-9]+)/edit/$', views.materia_editar, name='materia_editar'),
    url(r'^grado/(?P<pk>\d+)/remove/$', views.materia_eliminar, name='materia_eliminar'),

    url(r'^materia/$', views.lista_alumnos, name ='lista_alumnos'),
    url(r'^materia/nueva/$', views.alumno_nuevo, name='alumno_nuevo'),
    url(r'^materia/(?P<pk>[0-9]+)/$', views.alumno_detalle, name='alumno_detalle'),
    url(r'^materia/(?P<pk>[0-9]+)/edit/$', views.alumno_editar, name='alumno_editar'),
    url(r'^materia/(?P<pk>\d+)/remove/$', views.alumno_eliminar, name='alumno_eliminar'),

    url(r'^profesores/$', views.lista_tipo, name ='lista_tipo'),
    url(r'^profesores/nuevo/$', views.tipo_nuevo, name='tipo_nuevo'),
    url(r'^profesores/(?P<pk>[0-9]+)/$', views.tipo_detalle, name='tipo_detalle'),
    url(r'^profesores/(?P<pk>[0-9]+)/edit/$', views.tipo_editar, name='tipo_editar'),
    url(r'^profesores/(?P<pk>\d+)/remove/$', views.tipo_eliminar, name='tipo_eliminar'),

]

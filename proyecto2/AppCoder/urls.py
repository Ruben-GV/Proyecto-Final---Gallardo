from django.urls import path
from .views import *
from AppCoder import views


urlpatterns = [
    
    path("", inicioApp, name="inicioApp"),
    #path("crear_curso/", crear_curso),
    path("cursos/", cursos, name="cursos"),
    path("profesores/", profesores, name="profesores"),
    path("estudiantes/", estudiantes, name="estudiantes"),
    path("entregables/", entregables, name="entregables"),
    #path('busquedaCurso', views.busquedaCurso, name="BusquedaCurso"),
    path('buscar/', views.buscar),

    path("eliminarProfesor/<id>", eliminarProfesor, name="eliminarProfesor"),
    path("editarProfesor/<id>", editarProfesor, name="editarProfesor"),

    path("estudiante/list/", EstudianteList.as_view(), name="estudiante_list"),
    path("estudiante/nuevo", EstudianteCreacion.as_view(), name="estudiante_crear"),
    path("estudiante/<pk>", EstudianteDetalle.as_view(), name="estudiante_detalle"),
    path("estudiante/editar/<pk>", EstudianteUpdate.as_view(), name="estudiante_editar"),
    path("estudiante/borrar/<pk>", EstudianteDelete.as_view(), name="estudiante_borrar"),
]
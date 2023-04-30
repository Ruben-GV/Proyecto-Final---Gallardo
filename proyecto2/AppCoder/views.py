from django.shortcuts import render
from .models import Curso, Profesor, Estudiante, Entregable
from django.http import HttpResponse
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

"""
def crear_curso(request):

    nombre_curso="Programacion"
    comision_curso=10010
    print("Creando curso")
    curso=Curso(nombre=nombre_curso, comision=comision_curso)
    curso.save()
    respuesta=f"Curso creado--- {nombre_curso} - {comision_curso}"
    return HttpResponse(respuesta)
"""
    
def cursos(request):
    if request.method == "POST":
        form = Cursoform(request.POST)
        if form.is_valid():
            curso = Curso()
            curso.nombre = form.cleaned_data['nombre']
            curso.comision = form.cleaned_data['comision']
            curso.save()
            form = Cursoform()
    else:
        form = Cursoform()

    cursos = Curso.objects.all()
    context = {"cursos": cursos, "form": form}
    return render(request, "AppCoder/cursos.html",context)

def profesores(request):

    if request.method == "POST":
        form = Profesorform(request.POST)
        if form.is_valid():
            profesor = Profesor()
            profesor.nombre = form.cleaned_data['nombre']
            profesor.apellido = form.cleaned_data['apellido']
            profesor.email = form.cleaned_data['email']
            profesor.profesion = form.cleaned_data['profesion']
            profesor.save()
            form = Profesorform()
    else:
        form = Profesorform()

    #profesores = Profesor.objects.filter(nombre__icontains="p").all()
    profesores = Profesor.objects.all()
    context = {"profesores": profesores, "form": form}
    return render(request, "AppCoder/profesores.html",context)

def estudiantes(request):
    if request.method == "POST":
        form = Estudianteform(request.POST)
        if form.is_valid():
            estudiante = Estudiante()
            estudiante.nombre = form.cleaned_data['nombre']
            estudiante.apellido = form.cleaned_data['apellido']
            estudiante.email = form.cleaned_data['email']
            estudiante.save()
            form = Estudianteform()
    else:
        form = Estudianteform()

    #profesores = Profesor.objects.filter(nombre__icontains="p").all()
    estudiantes = Estudiante.objects.all()
    context = {"estudiantes": estudiantes, "form": form}
    return render(request, "AppCoder/estudiantes.html",context)

def entregables(request):
    if request.method == "POST":
        form = Entregableform(request.POST)
        if form.is_valid():
            entregable = Entregable()
            entregable.nombre = form.cleaned_data['nombre']
            entregable.fecha_entrega = form.cleaned_data['fecha_entrega']
            entregable.entregado = form.cleaned_data['entregado']
            entregable.save()
            form = Entregableform()
    else:
        form = Entregableform()

    entregables = Entregable.objects.all()
    context = {"entregables": entregables, "form": form}
    return render(request, "AppCoder/entregables.html",context)

def inicio(request):
    return HttpResponse("Bienvenido a la pagina principal")

def inicioApp(request):
    return render(request, "AppCoder/inicio.html")

#def busquedaCurso(request):
   # return render(request, "AppCoder/busquedaCurso.html")

def buscar(request):

    if request.GET["comision"]:
        comision = request.GET['comision']
        cursos = Curso.objects.filter(comision__icontains=comision)
        #respuesta = f"Estoy buscando la comisión nro: {request.GET['comision']}"

        return render(request, "AppCoder/resultadosBusqueda.html", {"cursos":cursos, "comision":comision})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)

def eliminarProfesor(request, id):
    profesor=Profesor.objects.get(id=id)
    print(profesor)
    profesor.delete()
    profesores=Profesor.objects.all()
    form = Profesorform()
    return render(request, "AppCoder/Profesores.html", {"profesores": profesores, "mensaje": "Profesor eliminado correctamente", "form": form})

def editarProfesor(request, id):
    profesor=Profesor.objects.get(id=id)
    if request.method=="POST":
        form = Profesorform(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            profesor.nombre=info["nombre"]
            profesor.apellido=info["apellido"]
            profesor.email=info["email"]
            profesor.profesion=info["profesion"]
            profesor.save()
            profesores=Profesor.objects.all()
            form = Profesorform()
            return render(request, "AppCoder/Profesores.html", {"profesores": profesores, "mensaje": "Profesor editado correctamente"})
        pass
    else:
        formulario = Profesorform(initial={"nombre":profesor.nombre, "apellido":profesor.apellido, "email":profesor.email, "profesion":profesor.profesion})
        return render(request, "AppCoder/editarProfesor.html", {"form": formulario, "profesor": profesor})
    
# Vistas basadas en clases

class EstudianteList(ListView):
    model= Estudiante
    template_name= "AppCoder/estudiantes.html"

class EstudianteCreacion(CreateView):
    model= Estudiante
    success_url= reverse_lazy("estudiante_list")
    fields=['nombre', 'apellido', 'email']

class EstudianteDetalle(DetailView):
    model= Estudiante
    template_name="AppCoder/estudiante_detalle.html"

class EstudianteUpdate(UpdateView):
    model = Estudiante
    success_url = reverse_lazy("estudiante_list")
    fields=['nombre', 'apellido', 'email']

class EstudianteDelete(DeleteView):
    model = Estudiante
    success_url = reverse_lazy('estudiante_list')
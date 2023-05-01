from django.shortcuts import render
from .models import Curso, Profesor, Estudiante, Entregable, Avatar
from django.http import HttpResponse
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#para el login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
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
@login_required
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
    avatar= Avatar.objects.filter(user=request.user.id)[0].imagen.url
    context = {"cursos": cursos, "form": form, "avatar": avatar}
    return render(request, "AppCoder/cursos.html",context)

@login_required
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

    avatar= Avatar.objects.filter(user=request.user.id)[0].imagen.url

    context = {"profesores": profesores, "form": form, "avatar":avatar}
    return render(request, "AppCoder/profesores.html",context)

@login_required
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
    avatar= Avatar.objects.filter(user=request.user.id)[0].imagen.url
    context = {"estudiantes": estudiantes, "form": form, "avatar":avatar}
    return render(request, "AppCoder/estudiantes.html",context)

@login_required
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
    avatar= Avatar.objects.filter(user=request.user.id)[0].imagen.url
    context = {"entregables": entregables, "form": form, "avatar":avatar}
    return render(request, "AppCoder/entregables.html",context)

def inicio(request):
    return HttpResponse("Bienvenido a la pagina principal")

def inicioApp(request):
    return render(request, "AppCoder/inicio.html", {"avatar":obtenerAvatar(request)})

#def busquedaCurso(request):
   # return render(request, "AppCoder/busquedaCurso.html")

def obtenerAvatar(request):
    avatar= Avatar.objects.filter(user=request.user.id)
    if len(avatar)!=0:
        return avatar[0].imagen.url
    else:
        return "media/avatars/default.png"

def buscar(request):

    if request.GET["comision"]:
        comision = request.GET['comision']
        cursos = Curso.objects.filter(comision__icontains=comision)
        #respuesta = f"Estoy buscando la comisión nro: {request.GET['comision']}"

        return render(request, "AppCoder/resultadosBusqueda.html", {"cursos":cursos, "comision":comision})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)

@login_required
def eliminarProfesor(request, id):
    profesor=Profesor.objects.get(id=id)
    print(profesor)
    profesor.delete()
    profesores=Profesor.objects.all()
    form = Profesorform()
    return render(request, "AppCoder/Profesores.html", {"profesores": profesores, "mensaje": "Profesor eliminado correctamente", "form": form})

@login_required
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

def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usu=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usu, password=clave) #Verifica si el usuario existe
            if usuario is not None:
                login(request, usuario)
                return render(request, "AppCoder/inicio.html", {"mensaje":f"Usuario {usu} logueado correctamente"})
            else:
                return render(request, "AppCoder/login.html", {"form":form, "mensaje":"Usuario o contraseña incorrectos"})
        else:
            return render(request, "AppCoder/login.html", {"form":form, "mensaje":"Usuario o contraseña incorrectos"})
    else:
        form=AuthenticationForm()
        return render(request, "AppCoder/login.html", {"form":form})
    
def register(request):
    if request.method=="POST":

        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "AppCoder/inicio.html", {"mensaje":f"Usuario {username} creado correctamente :)"})
        else:
            return render(request, "AppCoder/register.html", {"form":form, "mensaje":"Error al crear el usuario"})
    else:
        form = RegistroUsuarioForm()
    
    return render(request, "AppCoder/register.html", {"form":form})

@login_required
def editarPerfil(request):
    usuario=request.user

    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save()
            return render(request, "AppCoder/inicio.html", {"mensaje":f"Usuario {usuario.username} editado correctamente"})
        else:
            return render(request, "AppCoder/editarPerfil.html", {"form": form, "nombreusuario":usuario.username})
    else:
        form=UserEditForm(instance=usuario)
        avatar= Avatar.objects.filter(user=request.user.id)[0].imagen.url
        return render(request, "AppCoder/editarPerfil.html", {"form":form, "nombreusuario":usuario.username, "avatar":avatar})

@login_required
def agregarAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)>0:
                avatarViejo[0].delete()
            avatar.save()
            return render(request, "AppCoder/inicio.html", {"mensaje":f"Avatar agregado correctamente", "avatar":obtenerAvatar(request)})
        else:
            return render(request, "AppCoder/agregarAvatar.html", {"form":form, "usuario":request.user, "mensaje":"Error al agregar el avatar"})
    else:
        form=AvatarForm()
        return render(request, "AppCoder/agregarAvatar.html", {"form": form, "usuario": request.user, "avatar":obtenerAvatar(request)})
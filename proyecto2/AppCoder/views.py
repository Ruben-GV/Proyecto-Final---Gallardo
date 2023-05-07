from django.forms.models import BaseModelForm
from django.shortcuts import render
from .models import Avatar, Camiseta, Pantalon, Zapato, Abrigo, Comentario
from django.http import HttpResponse
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#para el login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.


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

@login_required
def camisetas(request):
    if request.method == "POST":
        form = CamisetaForm(request.POST)
        if form.is_valid():
            camiseta = Camiseta()
            camiseta.nombre = form.cleaned_data['nombre']
            camiseta.marca = form.cleaned_data['marca']
            camiseta.precio = form.cleaned_data['precio']
            camiseta.telefono = form.cleaned_data['telefono']
            camiseta.email = form.cleaned_data['email']
            camiseta.save()
            form = CamisetaForm()
    else:
        form = CamisetaForm()
    camisetas = Camiseta.objects.all()
    avatar= Avatar.objects.filter(user=request.user.id)[0].imagen.url
    context = {"camisetas": camisetas, "form": form, "avatar":avatar}
    return render(request, "AppCoder/camiseta.html",context)

class CamisetaList(ListView):
    model= Camiseta
    template_name= "AppCoder/camiseta.html"

class CamisetaAgregar(CreateView):
    model= Camiseta
    success_url= reverse_lazy("camiseta_list")
    fields=['nombre', 'marca', 'talla', 'precio', 'telefono', 'email', 'imagenCamiseta']

class CamisetaDetalle(DetailView):
    model= Camiseta
    template_name="AppCoder/camiseta_detalle.html"

class CamisetaUpdate(UpdateView):
    model = Camiseta
    form_class = ActualizacionCamiseta
    success_url = reverse_lazy('camiseta_list')
    template_name = 'AppCoder/camiseta_editar.html'

class CamisetaDelete(DeleteView):
    model = Camiseta
    success_url = reverse_lazy('camiseta_list')


@login_required
def pantalones(request):
    if request.method == "POST":
        form = PantalonForm(request.POST)
        if form.is_valid():
            pantalon = Pantalon()
            pantalon.nombre = form.cleaned_data['nombre']
            pantalon.marca = form.cleaned_data['marca']
            pantalon.talla = form.cleaned_data['talla']
            pantalon.precio = form.cleaned_data['precio']
            pantalon.telefono = form.cleaned_data['telefono']
            pantalon.email = form.cleaned_data['email']
            pantalon.save()
            form = PantalonForm()
    else:
        form = PantalonForm()
    pantalones = Pantalon.objects.all()
    avatar= Avatar.objects.filter(user=request.user.id)[0].imagen.url
    context = {"pantalones": pantalones, "form": form, "avatar":avatar}
    return render(request, "AppCoder/pantalones.html",context)

class PantalonList(ListView):
    model= Pantalon
    template_name= "AppCoder/pantalones.html"

class PantalonAgregar(CreateView):
    model= Pantalon
    success_url= reverse_lazy("pantalon_list")
    fields=['nombre', 'marca', 'talla', 'precio', 'telefono', 'email', 'imagenPantalon']

class PantalonDetalle(DetailView):
    model= Pantalon
    template_name="AppCoder/pantalon_detalle.html"

class PantalonUpdate(UpdateView):
    model = Pantalon
    form_class = ActualizacionPantalon
    success_url = reverse_lazy('pantalon_list')
    template_name = 'AppCoder/pantalon_editar.html'

class PantalonDelete(DeleteView):
    model = Pantalon
    success_url = reverse_lazy("pantalon_list")

@login_required
def zapatos(request):
    if request.method == "POST":
        form = ZapatoForm(request.POST)
        if form.is_valid():
            zapato = Zapato()
            zapato.nombre = form.cleaned_data['nombre']
            zapato.marca = form.cleaned_data['marca']
            zapato.talla = form.cleaned_data['talla']
            zapato.precio = form.cleaned_data['precio']
            zapato.telefono = form.cleaned_data['telefono']
            zapato.email = form.cleaned_data['email']
            zapato.save()
            form = ZapatoForm()
    else:
        form =  ZapatoForm()
    zapatos = Zapato.objects.all()
    avatar= Avatar.objects.filter(user=request.user.id)[0].imagen.url
    context = {"zapatos": zapatos, "form": form, "avatar":avatar}
    return render(request, "AppCoder/zapatos.html",context)

class ZapatoList(ListView):
    model= Zapato
    template_name= "AppCoder/zapatos.html"

class ZapatoAgregar(CreateView):
    model= Zapato
    success_url= reverse_lazy("zapato_list")
    fields=['nombre', 'marca', 'talla', 'precio', 'telefono', 'email', 'imagenZapato']

class ZapatoDetalle(DetailView):
    model= Zapato
    template_name="AppCoder/zapato_detalle.html"

class ZapatoUpdate(UpdateView):
    model = Zapato
    form_class = ActualizacionZapato
    success_url = reverse_lazy('zapato_list')
    template_name = 'AppCoder/zapato_editar.html'

class ZapatoDelete(DeleteView):
    model = Zapato
    success_url = reverse_lazy("zapato_list")

@login_required
def abrigos(request):
    if request.method == "POST":
        form = AbrigoForm(request.POST)
        if form.is_valid():
            abrigo = Abrigo()
            abrigo.nombre = form.cleaned_data['nombre']
            abrigo.marca = form.cleaned_data['marca']
            abrigo.talla = form.cleaned_data['talla']
            abrigo.precio = form.cleaned_data['precio']
            abrigo.telefono = form.cleaned_data['telefono']
            abrigo.email = form.cleaned_data['email']
            abrigo.save()
            form = AbrigoForm()
    else:
        form =  AbrigoForm()
    abrigos = Abrigo.objects.all()
    avatar= Avatar.objects.filter(user=request.user.id)[0].imagen.url
    context = {"abrigos": abrigos, "form": form, "avatar":avatar}
    return render(request, "AppCoder/abrigos.html",context)

class AbrigoList(ListView):
    model= Abrigo
    template_name= "AppCoder/abrigos.html"

class AbrigoAgregar(CreateView):
    model= Abrigo
    success_url= reverse_lazy("abrigo_list")
    fields=['nombre', 'marca', 'talla', 'precio', 'telefono', 'email', 'imagenAbrigo']

class AbrigoDetalle(DetailView):
    model= Abrigo
    template_name="AppCoder/abrigo_detalle.html"

class AbrigoUpdate(UpdateView):
    model = Abrigo
    form_class = ActualizacionAbrigo
    success_url = reverse_lazy('abrigo_list')
    template_name = 'AppCoder/abrigo_editar.html'

class AbrigoDelete(DeleteView):
    model = Abrigo
    success_url = reverse_lazy("abrigo_list")

@login_required
def comentarios(request):
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = Comentario()
            comentario.nombre = form.cleaned_data['nombre']
            comentario.mensaje = form.cleaned_data['mensaje']
            comentario.save()
            form = ComentarioForm()
    else:
        form =  ComentarioForm()
    comentarios = Comentario.objects.all()
    avatar= Avatar.objects.filter(user=request.user.id)[0].imagen.url
    context = {"comentarios": comentarios, "form": form, "avatar":avatar}
    return render(request, "AppCoder/comentario.html",context)

@login_required
def crear_comentario(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = Comentario()
            comentario.nombre = form.cleaned_data['nombre']
            comentario.mensaje = form.cleaned_data['mensaje']
            comentario.save()
            form = ComentarioForm()
    else:
        form = ComentarioForm()
    avatar= Avatar.objects.filter(user=request.user.id)[0].imagen.url
    context = {"comentarios": comentarios, "form": form, "avatar":avatar}
    return render(request, "AppCoder/comentario.html",context)


@login_required
def buscarCamiseta(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']
        camisetas = Camiseta.objects.filter(nombre__icontains=nombre)

        return render(request, "AppCoder/resultadosBusquedaCamiseta.html", {"camisetas":camisetas, "nombre":nombre})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)


def sobreMi(request):
    return render(request, 'AppCoder/sobreMi.html', {})

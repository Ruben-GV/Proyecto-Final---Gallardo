from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppCoder.models import *


class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(label="Email usuario")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields=["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Email usuario")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    first_name=forms.CharField(label="Modificar Nombre")
    last_name=forms.CharField(label="Modificar Apellido")

    class Meta:
        model = User
        fields=["username", "email", "password1", "password2", "first_name", "last_name"]
        help_texts = {k:"" for k in fields}

class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")


class CamisetaForm(forms.Form):
    nombre = forms.CharField(max_length=200, label="Nombre")
    marca = forms.CharField(max_length=40, label="Marca")
    talla = forms.CharField(max_length=40, label="Talla")
    precio = forms.DecimalField(max_digits=10, decimal_places=2,label="Precio")
    telefono = forms.IntegerField(label="Telefono")
    email = forms.EmailField()
    imagenPolo = forms.ImageField(label="Imagen")

class PantalonForm(forms.Form):
    nombre = forms.CharField(max_length=200, label="Nombre")
    marca = forms.CharField(max_length=40, label="Marca")
    talla = forms.CharField(max_length=40, label="Talla")
    precio = forms.DecimalField(max_digits=10, decimal_places=2,label="Precio")
    telefono= forms.IntegerField(label="Telefono")
    email = forms.EmailField()
    imagenPantalon = forms.ImageField(label="Imagen")

class ZapatoForm(forms.Form):
    nombre = forms.CharField(max_length=200, label="Nombre")
    marca = forms.CharField(max_length=40, label="Marca")
    talla = forms.CharField(max_length=40, label="Talla")
    precio = forms.DecimalField(max_digits=10, decimal_places=2,label="Precio")
    telefono= forms.IntegerField(label="Telefono")
    email = forms.EmailField()
    imagenZapato = forms.ImageField(label="Imagen del Zapato")

class ZapatillaForm(forms.Form):
    nombre = forms.CharField(max_length=200, label="Nombre")
    marca = forms.CharField(max_length=40, label="Marca")
    talla = forms.CharField(max_length=40, label="Talla")
    precio = forms.DecimalField(max_digits=10, decimal_places=2,label="Precio")
    telefono= forms.IntegerField(label="Telefono")
    email = forms.EmailField()
    imagenZapatilla = forms.ImageField(label="Imagen de la Zapatilla")

class AbrigoForm(forms.Form):
    nombre = forms.CharField(max_length=200, label="Nombre")
    marca = forms.CharField(max_length=40, label="Marca")
    talla = forms.CharField(max_length=40, label="Talla")
    precio = forms.DecimalField(max_digits=10, decimal_places=2,label="Precio")
    telefono= forms.IntegerField(label="Telefono")
    email = forms.EmailField()
    imagenAbrigo = forms.ImageField(label="Imagen del Abrigo")

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('nombre', 'mensaje')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje' : forms.Textarea(attrs={'class': 'form-control'}),
        }

class ActualizacionAbrigo(forms.ModelForm):
    class Meta:
        model = Abrigo
        fields = ('nombre', 'marca', 'talla', 'precio', 'telefono', 'email', 'imagenAbrigo')

        widgets = {
            'nombre' : forms.TextInput(attrs={'class': 'form-control'}),
            'marca' : forms.TextInput(attrs={'class': 'form-control'}),
            'talla' : forms.TextInput(attrs={'class': 'form-control'}),
            'precio' : forms.TextInput(attrs={'class': 'form-control'}),
            'telefono' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.TextInput(attrs={'class': 'form-control'}),
        }

class ActualizacionCamiseta(forms.ModelForm):
    class Meta:
        model = Camiseta
        fields = ('nombre', 'marca', 'talla', 'precio', 'telefono', 'email', 'imagenCamiseta')

        widgets = {
            'nombre' : forms.TextInput(attrs={'class': 'form-control'}),
            'marca' : forms.TextInput(attrs={'class': 'form-control'}),
            'talla' : forms.TextInput(attrs={'class': 'form-control'}),
            'precio' : forms.TextInput(attrs={'class': 'form-control'}),
            'telefono' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.TextInput(attrs={'class': 'form-control'}),
        }

class ActualizacionZapato(forms.ModelForm):
    class Meta:
        model = Zapato
        fields = ('nombre', 'marca', 'talla', 'precio', 'telefono', 'email', 'imagenZapato')

        widgets = {
            'nombre' : forms.TextInput(attrs={'class': 'form-control'}),
            'marca' : forms.TextInput(attrs={'class': 'form-control'}),
            'talla' : forms.TextInput(attrs={'class': 'form-control'}),
            'precio' : forms.TextInput(attrs={'class': 'form-control'}),
            'telefono' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.TextInput(attrs={'class': 'form-control'}),
        }

class ActualizacionPantalon(forms.ModelForm):
    class Meta:
        model = Pantalon
        fields = ('nombre', 'marca', 'talla', 'precio', 'telefono', 'email', 'imagenPantalon')

        widgets = {
            'nombre' : forms.TextInput(attrs={'class': 'form-control'}),
            'marca' : forms.TextInput(attrs={'class': 'form-control'}),
            'talla' : forms.TextInput(attrs={'class': 'form-control'}),
            'precio' : forms.TextInput(attrs={'class': 'form-control'}),
            'telefono' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.TextInput(attrs={'class': 'form-control'}),
        }

    
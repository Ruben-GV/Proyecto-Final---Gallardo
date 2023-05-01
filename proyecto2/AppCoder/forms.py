from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Profesorform(forms.Form):
    nombre= forms.CharField(max_length=50, label="Nombre")
    apellido= forms.CharField(max_length=50, label="Apellidos")
    email= forms.EmailField()
    profesion= forms.CharField(max_length=50, label="Profesión")

class Estudianteform(forms.Form):
    nombre= forms.CharField(max_length=50, label="Nombre")
    apellido= forms.CharField(max_length=50, label="Apellidos")
    email= forms.EmailField()

class Cursoform(forms.Form):
    nombre= forms.CharField(max_length=50, label="Nombre")
    comision= forms.CharField(max_length=50, label="Comisión")

class Entregableform(forms.Form):
    nombre= forms.CharField(max_length=50, label="Nombre")
    fecha_entrega= forms.DateField()
    entregado= forms.BooleanField()

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
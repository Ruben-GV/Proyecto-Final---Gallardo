from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Avatar(models.Model):
    imagen= models.ImageField(upload_to="avatars", default='avatars/avatar.png')
    user=models.ForeignKey(User, on_delete=models.CASCADE)

class Camiseta(models.Model):
    #usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=200, default='')
    marca = models.CharField(max_length=40, default='')
    talla = models.CharField(max_length=40, default='')
    precio = models.DecimalField(max_digits=10, decimal_places=2, default='')
    telefono= models.IntegerField(default='')
    email = models.EmailField(default='')
    imagenCamiseta = models.ImageField(null=True, blank=True, upload_to="ropa", default='')
    
    def __str__(self):
        return f"{self.nombre} {self.marca}"
    
class Pantalon(models.Model):
    #usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=200)
    marca = models.CharField(max_length=40)
    talla = models.CharField(max_length=40)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    telefono= models.IntegerField()
    email = models.EmailField()
    imagenPantalon = models.ImageField(null=True, blank=True, upload_to="ropa")
    
    def __str__(self):
        return f"{self.nombre} {self.marca}"
    
class Zapato(models.Model):
    #usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=200)
    marca = models.CharField(max_length=40)
    talla = models.CharField(max_length=40)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    telefono= models.IntegerField()
    email = models.EmailField()
    imagenZapato = models.ImageField(null=True, blank=True, upload_to="ropa")
    
    def __str__(self):
        return f"{self.nombre} {self.marca}"
    
class Abrigo(models.Model):
    #usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=200)
    marca = models.CharField(max_length=40)
    talla = models.CharField(max_length=40)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    telefono= models.IntegerField()
    email = models.EmailField()
    imagenAbrigo = models.ImageField(null=True, blank=True, upload_to="ropa")
    
    def __str__(self):
        return f"{self.nombre} {self.marca}"
    
class Comentario(models.Model):
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.fechaComentario)

class Mensaje(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.mensaje

    class Meta:
        ordering = ('timestamp',)
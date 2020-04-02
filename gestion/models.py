from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Inicio(models.Model):
    fecha=models.DateTimeField(auto_now_add=True)
    imagen=models.ImageField(blank=True, null=True)
    descripcion=models.CharField(max_length=100, blank=True, null=True)
    autor= models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    #slug= models.SlugField(unique=True, default=None)
      
    def __str__(self):
        return str(self.imagen)

class Perfil(models.Model):
    autor= models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    nombre=models.CharField(max_length=100,blank=True, null=True)
    imagenPerfil=models.ImageField(upload_to='images_perfil',blank=True)
    infoCuenta=models.CharField(max_length=100)
    

    def __str__(self):
        return str(self.autor)


class Publicaciones(models.Model):
    fecha=models.DateTimeField(auto_now_add=True)
    imagen=models.ForeignKey(Inicio,on_delete=models.CASCADE,default=None,blank=True,null=True)
    comentarios=models.CharField(max_length=100, blank=True, null=True)
    likes=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(1)], blank=True, null=True)







     



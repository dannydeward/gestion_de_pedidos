from distutils.command.upload import upload
from email.headerregistry import ContentDispositionHeader
from ssl import create_default_context
from tabnanny import verbose
from tkinter import image_names
from django.db import models

# Create your models here.

class Servicios(models.Model):
    Titulo= models.CharField(max_length=50)
    Contenido= models.CharField(max_length=50)
    Imagen= models.ImageField(upload_to='Servicios')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    class meta():
        verbose_name='Servicios'
        verbose_name_plural='Servicios'
        
        
        def __str__(self):
            return self.titulo
    
    
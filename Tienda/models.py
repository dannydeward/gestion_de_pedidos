from distutils.command.upload import upload
from http.client import PRECONDITION_FAILED
from mailbox import NoSuchMailboxError
from tkinter import CASCADE
from django.db import models

from Blog.views import categoria

# Create your models here.
class CategoriaProd(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name="CategoriaProd"
        verbose_name_plural="CategroiasProd"
        
    def __str__(self):
        return self.nombre
    

class Producto(models.Model):
    nombre =models.CharField(max_length=50)
    categoria=models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="tinda", null= True, blank=True) 
    precio= models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
       verbose_name="Producto"
       verbose_name_plural="Productos"
         
    
    
from django.contrib import admin
from .models import Categoria, Post


# Register your models here.

class Categoriaadmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    


class Postadmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    
    
admin.site.register( Categoria, Categoriaadmin)

admin.site.register( Post, Postadmin)

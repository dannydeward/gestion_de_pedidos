from django import forms

class FormularioContacto(forms.Form):
    nombre= forms.CharField(label='Nombre', required=True ,max_length=100 )
    email= forms.CharField(label='E-mail', required=True)
    contenido= forms.CharField(label='Contenido', max_length=500, widget=forms.Textarea)
    
    
    
    
    
    
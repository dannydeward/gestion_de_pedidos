from django.shortcuts import redirect, render
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.


def contacto (request):
      Formulario_Contacto= FormularioContacto()          
      if request.method=="POST": 
             Formulario_Contacto= FormularioContacto(data=request.POST) 
             if Formulario_Contacto.is_valid():
                    nombre=request.POST.get("nombre")
                    email=request.POST.get("email")
                    contenido=request.POST.get("contenido")
                  
                  
                    email= EmailMessage("mensaje desde App Django",
                                       "el ususuario con nombre {} con la direccion {} escribe lo siguiente:\n\n {} ".format(nombre,email,contenido),
                                        "contacto/",
                                        ["pildorasdepaython@gmail.com"], reply_to=[email])
             try:
                    email.send()
                    return redirect("./?valido")
             except:
                           return redirect("./?novalido")
                                                        
                                
                  
                  
       
      return render(request, 'Contacto/contacto.html',{'formulario': Formulario_Contacto})                                          



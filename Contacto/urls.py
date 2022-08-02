from django.urls import path
from Contacto import views



urlpatterns = [
    
        path('contacto/', views.contacto, name= 'Contacto'),
    
]


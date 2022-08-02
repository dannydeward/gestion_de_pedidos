from django.urls import path
from Blog import views


urlpatterns = [
       
    path('blog',views.blog, name='Blog'),
    path('blog/categoria/<int:categoria_id>', views.categoria, name='categoria')
]
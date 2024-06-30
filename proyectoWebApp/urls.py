from django.urls import path
from proyectoWebApp import views

urlpatterns = [
    path('', views.index, name="Inicio"),
    path('servicios', views.servicios, name="Servicios"),
    path('tienda', views.tienda, name="Tienda"),
    path('Blog', views.blog, name="Blog"),
    path('contacto', views.contacto, name="Contacto"),
]
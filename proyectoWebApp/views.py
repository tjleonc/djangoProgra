from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request,'ProyectoWebApp/index.html')

def servicios(request):
    return render(request,'ProyectoWebApp/servicios.html')

def tienda(request):
    return render(request,'ProyectoWebApp/tienda.html')

def blog(request):
    return render(request,'ProyectoWebApp/blog.html')

def contacto(request):
    return render(request,'ProyectoWebApp/contacto.html')




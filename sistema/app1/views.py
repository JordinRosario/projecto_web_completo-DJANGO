from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def servicios(request):
    return render(request, './app1/servicio.html')


def tienda(request):
    return render(request, './app1/tienda.html')

def blog(request):
    return render(request, './app1/blog.html')

def contacto(request):
    return render(request, './app1/contacto.html')


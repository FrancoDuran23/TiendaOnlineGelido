from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return render(request, "StoreOnlineApp/home.html")
def servicios(request):
    return render(request, "StoreOnlineApp/servicio.html")
def productos(request):
    return render(request, "StoreOnlineApp/producto.html")
def sabores(request):
    return render(request, "StoreOnlineApp/sabor.html")
def blog(request):
    return render(request, "StoreOnlineApp/blog.html")   
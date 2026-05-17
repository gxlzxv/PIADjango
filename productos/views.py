from django.shortcuts import render
from .models import Producto

# Create your views here.
def prodindex(request):

    productos = Producto.objects.all()

    return render(request, 'productos/prodindex.html', {
        'productos': productos
    })
from django.shortcuts import render

# Create your views here.
def suindex (request):
    return render(request, 'sucursales/suindex.html')
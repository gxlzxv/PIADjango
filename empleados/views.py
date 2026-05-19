from django.shortcuts import render

# Create your views here.
def empindex (request):
    return render(request, 'empleados/empindex.html')
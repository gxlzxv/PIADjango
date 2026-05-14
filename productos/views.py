from django.shortcuts import render

# Create your views here.
def prodindex (request):
    return render(request, 'prodindex.html')
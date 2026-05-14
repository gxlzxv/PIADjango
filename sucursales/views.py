from django.shortcuts import render

# Create your views here.
def suindex (request):
    return render(request, 'suindex.html')
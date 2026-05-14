from django.shortcuts import render

# Create your views here.
def docindex (request):
    return render(request, 'docindex.html')
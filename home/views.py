from django.shortcuts import render
from django.http import JsonResponse
from pathlib import Path


def index(request):

    if request.method == 'POST':

        nombre = request.POST.get('nombre', '').strip()
        calificacion = request.POST.get('calificacion', '')
        resena = request.POST.get('resena', '').strip()

        if not nombre or not calificacion or not resena:
            return JsonResponse({
                'success': False,
                'mensaje': 'Por favor completa todos los campos.'
            })

        archivo = Path(__file__).resolve().parent.parent / 'resenas.txt'

        with open(archivo, 'a', encoding='utf-8') as f:
            f.write(f'Nombre: {nombre}\n')
            f.write(f'Calificación: {calificacion}/5\n')
            f.write(f'Reseña: {resena}\n')
            f.write('-' * 50 + '\n')

        return JsonResponse({
            'success': True,
            'mensaje': '¡Gracias por compartir tu opinión!'
        })

    return render(request, 'home/index.html')
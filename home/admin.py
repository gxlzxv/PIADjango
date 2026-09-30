from django.contrib import admin
from django.http import HttpResponse
from pathlib import Path


def ver_resenas(request):

    archivo = Path(__file__).resolve().parent.parent / 'resenas.txt'

    if archivo.exists():
        with open(archivo, 'r', encoding='utf-8') as f:
            contenido = f.read()
    else:
        contenido = 'Todavía no hay reseñas registradas.'

    return HttpResponse(
        f"""
        <html>
            <head>
                <title>Reseñas</title>
            </head>

            <body style="font-family: Arial; padding: 30px;">

                <h1>Reseñas registradas</h1>

                <pre style="
                    background: #f4f4f4;
                    padding: 20px;
                    border-radius: 8px;
                    white-space: pre-wrap;
                ">{contenido}</pre>

                <br>

                <a href="/admin/">Volver al administrador</a>

            </body>
        </html>
        """
    )
# PIADjango

1. Clonar el repositorio
Abran una terminal en la carpeta donde quieran guardar el proyecto y ejecuten:
git clone [https://github.com/gxlzxv/PIADjango.git](https://github.com/gxlzxv/PIADjango.git)
cd PIADjango

2. Crear el entorno virtual (venv)
Como el archivo .gitignore impide que se suba mi entorno virtual para no generar archivos basura, cada uno debe crear el suyo:

En Windows: python -m venv venv

Activar el entorno: .\venv\Scripts\activate

3. Instalar las dependencias
Una vez activado el entorno (verán el nombre (venv) en la terminal), instalen todas las librerías necesarias usando el archivo que genere:
pip install -r requirements.txt

4. Preparar la base de datos
Como no subi mi base de datos local db.sqlite3, deben crear la suya y aplicar la estructura del proyecto:
python manage.py migrate

5. Correr el servidor
Para verificar que todo está bien, ejecuten:
python manage.py runserver

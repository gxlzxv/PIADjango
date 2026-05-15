Conectar y usar

1. Entorno: python -m venv venv y activarlo.

2. Librerías: pip install -r requirements.txt

3. Base de datos: python manage.py migrate

4. Cargar los users: python manage.py loaddata permisos_y_usuarios.json (o el nombre que le hayas puesto al archivo).

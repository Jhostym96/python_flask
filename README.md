## Crear un entorno virtual
'''
python -m venv entorno_virtual
'''
## Activar el entorno virtual
'''
source entorno_virtual/Scripts/activate
'''
## Instalar Flask
'''
pip install flask
'''
## Correr la aplicacion de flask
'''
flask --debug run
'''
## Instalar sqlalchemy
'''
pip install Flask-SQLAlchemy
'''
## Registrar las dependencias que estamos usando
'''
pip freeze > requirements.txt
'''
## Migrar la base de datos
'''
pip install Flask-Migrate
flask db init
flask db migrate -m "generar migraciones"
flask db upgrade
'''
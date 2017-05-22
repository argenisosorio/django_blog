Proyecto tipo Blog en Django
===
## Detalles
* Incorpora autenticación de usuarios
* Crear, Actualizar, Eliminar y Detallar publicaciones
## Requerimientos
```python
Django==1.10.1
Python 2.7.3
```
## Ejecutar el proyecto
```python
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py makemigrations app_blog
$ python manage.py migrate
$ python manage.py runserver
```

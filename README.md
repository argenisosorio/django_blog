# Proyecto tipo Blog en Django

# Detalles
* Incorpora gestión de usuarios (autenticación, creación de cuentas)
* Crear, Actualizar, Eliminar y Detallar publicaciones

## Requerimientos
```
Python 2.7.3
Django==1.10.1
django-simple-captcha==0.5.5
```

## Desplegar el proyecto
```
$ pip install -r requirements.txt
$ python manage.py makemigrations app_blog
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateTimeField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


'''
 Crea un modelo llamado Usuario siguiendo el ERD anterior
 Crea y ejecuta los archivos de migración para crear la tabla Usuario en su base de datos.
 Crea un archivo .txt donde guardará cada una de las consultas que ejecutará en el shell
 Ejecuta el shell e importe su modelo de usuario
 Consulta: Crear 3 nuevos usuarios
 Consulta: recuperar todos los usuarios
 Consulta: recuperar el último usuario
 Consulta: recuperar el primer usuario
 Consulta: Cambie el usuario con id = 3 para que su apellido sea Pancakes.
 Consulta: Eliminar el usuario con id = 2 de la base de datos
 Consulta: Obtenga todos los usuarios, ordenados por su nombre
 BONUS Query: obtén todos los usuarios, ordenados por su nombre en orden descendente
 Envía tu archivo .txt que contiene todas las consultas que ejecutó en el shell
'''

class Usuario(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.TextField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



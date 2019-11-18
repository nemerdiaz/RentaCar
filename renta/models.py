from django.db import models

# Create your models here.

class DirOrigen(models.Model):
    comunaOrigen = models.CharField(max_length=50)    
    direccionOrigen = models.CharField(max_length=100)

    def __str__(self):
        return self.comunaOrigen

class DirDestino(models.Model):    
    comunaDestino = models.CharField(max_length=50)    
    direccionDestino = models.CharField(max_length=100)

    def __str__(self):
        return self.comunaDestino


class Persona(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    run = models.IntegerField(unique=True)
    correo = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

from django.db import models
from django.utils import timezone

# Create your models here.
class Musico(models.Model):
    nombre = models.CharField(max_length=20, primary_key=True)
    fec_nacimiento = models.DateField()
    instrumento = models.CharField(max_length=20, blank=True)
    grupos = models.ManyToManyField('Grupo', blank=True)

class Grupo(models.Model):
    nombre = models.CharField(max_length=20, primary_key=True)
    fec_fundacion = models.DateField()
    estilo = models.CharField(max_length=20)
    miembros = models.ManyToManyField(Musico)

class Album(models.Model):
    titulo = models.CharField(max_length=50)
    distribuidora = models.CharField(max_length=50)
    fec_lanzamiento = models.DateField()
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
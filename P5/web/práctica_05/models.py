from django.db import models
from django.utils import timezone

# Create your models here.
class Musico(models.Model):
    voz = "voz"
    piano = "piano"
    bajo = "bajo"
    bateria = "bateria"
    guitarra = "guitarra"
    instrumentos = (
            (voz, "voz"),
            (piano, "piano"),
            (bajo, "bajo"),
            (bateria, "bateria"),
            (guitarra, "guitarra"),
        )
    
    nombre = models.CharField(max_length=20, blank=False)
    fec_nacimiento = models.DateField(blank=False)
    instrumento = models.CharField(
        default=voz,
        choices=instrumentos,
        max_length= 30,
        blank=False,
    )
    grupos = models.ManyToManyField('Grupo', blank=True)

    def __str__(self):
        return '{}'.format(self.nombre)

    def serialize(self):
        return {"nombre": self.nombre,
                "fec_nacimiento": self.fec_nacimiento,
                "instrumento": self.instrumento}

class Grupo(models.Model):
    indie = "indie"
    pop = "pop"
    rock = "rock"
    estilos = (
            (indie, "indie"),
            (pop, "pop"),
            (rock, "rock"),
        )
    nombre = models.CharField(max_length=20, blank=False)
    fec_fundacion = models.DateField(blank=False)
    estilo = models.CharField(
        default=pop,
        choices=estilos,
        max_length= 30,
        blank=False,
    )
    miembros = models.ManyToManyField(Musico)
    
    def __str__(self):
        return '{}'.format(self.nombre)

class Album(models.Model):
    titulo = models.CharField(max_length=50, blank=False)
    distribuidora = models.CharField(max_length=50, blank=False)
    fec_lanzamiento = models.DateField(blank=False)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, blank=False)
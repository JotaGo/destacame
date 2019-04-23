from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Pasajero(models.Model):
    run = models.CharField(max_length=13)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)

class Chofer(models.Model):
    run = models.CharField(max_length=13)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)

class Trayecto(models.Model):
    nombre = models.CharField(max_length=30)
    horario = models.TimeField(auto_now=False, auto_now_add=False, null=False, blank=False)
    pasajeros = models.ManyToManyField(Pasajero, through='Asiento')

class Asiento(models.Model):
    trayectos = models.ForeignKey(Trayecto, on_delete=models.CASCADE)
    pasajeros = models.ForeignKey(Pasajero, on_delete=models.CASCADE)
    asientos = models.PositiveSmallIntegerField(
        unique=True,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
            ]
        )

class Bus(models.Model):
    matricula = models.CharField(max_length=10)
    piloto = models.OneToOneField(Chofer, null=True, blank=True, on_delete=models.SET_NULL)
    trayectos = models.ForeignKey(Trayecto, null=False, blank=False, on_delete=models.CASCADE)

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Pasajero(models.Model):
    run = models.CharField(max_length=13)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    def __str__(self):
        return self.run

class Chofer(models.Model):
    run = models.CharField(max_length=13)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    def __str__(self):
        return self.run

class Trayecto(models.Model):
    nombre = models.CharField(max_length=30)
    horario = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    pasajeros = models.ManyToManyField(Pasajero, through='Viaje')

    def __str__(self):
        return '{} {}'.format(self.nombre, self.horario)

class Viaje(models.Model):
    trayectos = models.ForeignKey(Trayecto, on_delete=models.CASCADE)
    pasajeros = models.ForeignKey(Pasajero, on_delete=models.CASCADE)
    # asientos = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))))
    fecha = models.DateField(auto_now=True, auto_now_add=False,)
    
    # class Meta:
    #     unique_together = ["trayectos","asientos","fecha"]
    
class Bus(models.Model):
    matricula = models.CharField(max_length=10)
    piloto = models.OneToOneField(Chofer, null=True, blank=True, on_delete=models.SET_NULL)
    trayectos = models.ForeignKey(Trayecto, null=False, blank=False, on_delete=models.CASCADE)
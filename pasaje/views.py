from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Pasajero, Trayecto

# Create your views here.

def index(request):
    lista_trayectos = Trayecto.objects.values('nombre').distinct()
    template = loader.get_template('pasaje/viajes_disponibles.html')
    context = {
        'lista_trayectos' : lista_trayectos,
    }
    return HttpResponse(template.render(context, request))

def avaliable_trayectos(request, trayecto_nombre):
    q = trayecto_nombre
    output = Trayecto.objects.filter(nombre='q')
    return HttpResponse("Este trayecto cubre el sector %s." % output[0].nombre)

def detalles(request, trayecto_id):
    return HttpResponse("Aqui se observara una lista con los Trayectos disponibles para que el pasajero pueda escoger")
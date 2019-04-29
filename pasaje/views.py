from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .models import Pasajero, Trayecto
from .forms import (TrayectoForm, PasajeroForm, ChoferForm, BusForm)

# Create your views here.

def index(request):
    lista_trayectos = Trayecto.objects.values('nombre').distinct()
    template = loader.get_template('pasaje/viajes_disponibles.html')
    context = {
        'lista_trayectos' : lista_trayectos,
    }
    return HttpResponse(template.render(context, request))

def avaliable_trayectos(request, trayecto_nombre):
    var = trayecto_nombre.split('-')
    a = []
    for items in var:
        a.append(items.capitalize())
    trayecto_n = ' '.join(a)
    horarios_trayecto = Trayecto.objects.filter(nombre=trayecto_n)
    template = loader.get_template('pasaje/horarios_disponibles.html')
    context = {
        'horarios_trayecto' : horarios_trayecto
    }
    return HttpResponse(template.render(context, request))

def detalles(request, trayecto_nombre):
    return HttpResponse("Aqui se observara una lista con los Trayectos disponibles para que el pasajero pueda escoger")

def administrar_trayectos(request):
    if request.method == 'POST':
        form = TrayectoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pasaje/')
    else:
        form = TrayectoForm()
    return render(request, 'pasaje/c_trayecto.html', {'form': form})

def administrar_buses(request):
    if request.method == 'POST':
        form = BusForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pasaje/')
    else:
        form = BusForm()
    return render(request, 'pasaje/c_bus.html', {'form': form})

def administrar_choferes(request):
    if request.method == 'POST':
        form = ChoferForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pasaje/')
    else:
        form = ChoferForm()
    return render(request, 'pasaje/c_chofer.html', {'form': form})

def administrar_pasajeros(request):
    if request.method == 'POST':
        form = PasajeroForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pasaje/')
    else:
        form = PasajeroForm()
    return render(request, 'pasaje/c_pasajero.html', {'form': form})
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .models import (Pasajero, Trayecto, Chofer, Bus, Viaje)
from .forms import (TrayectoForm, PasajeroForm, ChoferForm, BusForm, ViajeForm)

import datetime
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

def detalles(request, trayecto_id):
    trayecto = Trayecto.objects.get(id=trayecto_id)
    if request.method == 'POST':
        form = ViajeForm(request.POST)
        if form.is_valid():
            trayecto_f = form.data['trayectos']
            fecha_f = form.data['fecha']
            count = Viaje.objects.filter(trayectos=trayecto_f,fecha=fecha_f).count()
            if count <= 10:
                form.save()
                return redirect('index')
            else:
                return HttpResponse('El bus esta lleno, intenlo en otra fecha o tome otro bus')
    else:
        f = {
            'pasajeros': None,
            'trayectos': trayecto.id,
            'fecha': None,
        }
        form = ViajeForm(initial=f)
    return render(request, 'pasaje/viaje.html', {'form': form})

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

def read_trayectos(request):
    trayectos = Trayecto.objects.all().order_by('id')
    context = {'trayectos' : trayectos,}
    return render(request, 'pasaje/r_trayectos.html', context)

def read_pasajeros(request):
    pasajeros = Pasajero.objects.all().order_by('id')
    context = {'pasajeros' : pasajeros}
    return render(request, 'pasaje/r_pasajeros.html', context)

def read_choferes(request):
    choferes = Chofer.objects.all().order_by('id')
    context = {'choferes' : choferes}
    return render(request, 'pasaje/r_choferes.html', context)

def read_buses(request):
    buses = Bus.objects.all().order_by('id')
    context = {'buses' : buses}
    return render(request, 'pasaje/r_buses.html', context)

def modificar_trayecto(request, trayecto_id):
    trayecto = Trayecto.objects.get(id=trayecto_id)
    if request.method == 'GET':
        form = TrayectoForm(instance=trayecto)
    else:
        form = TrayectoForm(request.POST, instance=trayecto)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/pasaje/')
    return render(request, 'pasaje/c_trayecto.html', {'form':form})

def delete_trayecto(request, trayecto_id):
    trayecto = Trayecto.objects.get(id=trayecto_id)
    if request.method == 'POST' :
        trayecto.delete()
        return redirect('read_trayectos')
    return render(request, 'pasaje/d_trayecto.html', {'trayecto':trayecto})        

def modificar_bus(request, bus_id):
    bus = Bus.objects.get(id=bus_id)
    if request.method == 'GET':
        form = BusForm(instance=bus)
    else:
        form = BusForm(request.POST, instance=bus)
        if form.is_valid():
            form.save()
        return redirect('read_buses')
    return render(request, 'pasaje/c_bus.html', {'form':form})

def delete_bus(request, bus_id):
    bus = Bus.objects.get(id=bus_id)
    if request.method == 'POST' :
        bus.delete()
        return redirect('read_buses')
    return render(request, 'pasaje/d_bus.html', {'bus':bus})

def modificar_chofer(request, chofer_id):
    chofer = Chofer.objects.get(id=chofer_id)
    if request.method == 'GET':
        form = ChoferForm(instance=chofer)
    else:
        form = ChoferForm(request.POST, instance=chofer)
        if form.is_valid():
            form.save()
        return redirect('read_choferes')
    return render(request, 'pasaje/c_chofer.html', {'form':form})

def delete_chofer(request, chofer_id):
    chofer = Chofer.objects.get(id=chofer_id)
    if request.method == 'POST' :
        chofer.delete()
        return redirect('read_choferes')
    return render(request, 'pasaje/d_chofer.html', {'chofer':chofer})

def modificar_pasajero(request, pasajero_id):
    pasajero = Pasajero.objects.get(id=pasajero_id)
    if request.method == 'GET':
        form = PasajeroForm(instance=pasajero)
    else:
        form = PasajeroForm(request.POST, instance=pasajero)
        if form.is_valid():
            form.save()
        return redirect('read_pasajeros')
    return render(request, 'pasaje/c_pasajero.html', {'form':form})

def delete_pasajero(request, pasajero_id):
    pasajero = Pasajero.objects.get(id=pasajero_id)
    if request.method == 'POST' :
        pasajero.delete()
        return redirect('read_pasajeros')
    return render(request, 'pasaje/d_pasajero.html', {'pasajero':pasajero})
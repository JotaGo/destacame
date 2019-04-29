from django import forms
from django.forms import ModelForm
from pasaje.models import (Trayecto, Pasajero, Chofer, Bus)
from django.forms import (TextInput, TimeInput, Select)

class TrayectoForm(ModelForm):

    class Meta:
        model = Trayecto
        fields = [
            'nombre',
            'horario',
        ]

        labels = {
            'nombre': 'Trayecto',
            'horario': 'Horario',
        }
        
        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control'}),
            'horario': TimeInput(attrs={'class': 'form-control'}),
        }

class PasajeroForm(ModelForm):

    class Meta:
        model = Pasajero
        fields = [
            'run',
            'nombre',
            'apellido',
        ]

        labels = {
            'run' : 'run',
            'nombre' : 'nombre',
            'apellido' : 'apellido'
        }

        widgets = {
            'run' : TextInput(attrs={'class': 'form-control'}),
            'nombre' : TextInput(attrs={'class': 'form-control'}),
            'apellido' : TextInput(attrs={'class': 'form-control'})
        }

class ChoferForm(ModelForm):

    class Meta:
        model = Chofer
        fields = [
            'run',
            'nombre',
            'apellido',
        ]

        labels = {
            'run' : 'run',
            'nombre' : 'nombre',
            'apellido' : 'apellido'
        }

        widgets = {
            'run' : TextInput(attrs={'class': 'form-control'}),
            'nombre' : TextInput(attrs={'class': 'form-control'}),
            'apellido' : TextInput(attrs={'class': 'form-control'})
        }

class BusForm(ModelForm):

    class Meta:
        model = Bus
        fields = [
            'matricula',
            'piloto',
            'trayectos',
        ]

        labels = {
            'matricula' : 'matricula',
            'piloto' : 'chofer',
            'trayectos' : 'trayecto',
        }

        widgets = {
            'matricula' : TextInput(attrs={'class' : 'form-control'}),
            'piloto' : Select(attrs={'class' : 'form-control'}),
            'trayectos' : Select(attrs={'class' : 'form-control'}),
        }
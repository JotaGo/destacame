from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Trayecto)
admin.site.register(Pasajero)
admin.site.register(Asiento)
admin.site.register(Bus)
admin.site.register(Chofer)
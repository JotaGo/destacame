from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('administrar_trayectos/', views.administrar_trayectos, name='trayectos'),
    path('administrar_buses/', views.administrar_buses, name='crud_buses'),
    path('administrar_choferes/', views.administrar_choferes, name='choferes'),
    path('administrar_pasajeros/', views.administrar_pasajeros, name='pasajeros'),
    path('read_trayectos/', views.read_trayectos, name='read_trayectos'),
    path('<slug:trayecto_nombre>/', views.avaliable_trayectos, name='av_trayectos'),
    path('<slug:trayecto_nombre>/detalles/', views.detalles, name='viajes'),
]
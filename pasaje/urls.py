from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('administrar_trayectos/', views.administrar_trayectos, name='trayectos'),
    path('administrar_trayectos/<int:trayecto_id>/', views.modificar_trayecto, name='modificar_trayecto'),
    path('administrar_trayectos/<int:trayecto_id>/delete/', views.delete_trayecto, name='delete_trayecto'),
    path('administrar_buses/', views.administrar_buses, name='crud_buses'),
    path('administrar_buses/<int:bus_id>/', views.modificar_bus, name='modificar_bus'),
    path('administrar_buses/<int:bus_id>/delete/', views.delete_bus, name='delete_bus'),
    path('administrar_choferes/', views.administrar_choferes, name='choferes'),
    path('administrar_choferes/<int:chofer_id>/', views.modificar_chofer, name='modificar_chofer'),
    path('administrar_choferes/<int:chofer_id>/delete/', views.delete_chofer, name='delete_chofer'),
    path('administrar_pasajeros/', views.administrar_pasajeros, name='pasajeros'),
    path('administrar_pasajeros/<int:pasajero_id>/', views.modificar_pasajero, name='modificar_pasajero'),
    path('administrar_pasajeros/<int:pasajero_id>/delete/', views.delete_pasajero, name='delete_pasajero'),
    path('read_trayectos/', views.read_trayectos, name='read_trayectos'),
    path('read_pasajeros/', views.read_pasajeros, name='read_pasajeros'),
    path('read_choferes/', views.read_choferes, name='read_choferes'),
    path('read_buses/', views.read_buses, name='read_buses'),
    path('<slug:trayecto_nombre>/', views.avaliable_trayectos, name='av_trayectos'),
    path('<slug:trayecto_nombre>/promedio/', views.informacion, name='info_trayecto'),
    path('<int:trayecto_id>/detalles/', views.detalles, name='viajes'),
]
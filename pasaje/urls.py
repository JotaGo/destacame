from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:trayecto_nombre>/', views.avaliable_trayectos, name='av_trayectos'),
    path('<int:trayecto_id>/detalles/', views.detalles, name='viajes'),    
]
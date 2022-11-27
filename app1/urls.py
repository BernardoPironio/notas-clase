from django.urls import path
from app1.views import *


urlpatterns=[
    path('', inicio, name='inicio'),
    path('entrenadores/', entrenadores, name='entrenadores'),
    path('timoneles/', timoneles, name='timoneles'),
    path('tripulantes/', tripulantes, name='tripulantes'),
    path('busquedaentrenadores/', busquedaentrenadores, name='busquedaentrenadores'),
    path('buscar/', buscar,name='buscar'),
]
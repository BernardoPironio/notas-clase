from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request,'app1/inicio.html')

def entrenadores(request):
    return render(request,'app1/entrenadores.html')

def timoneles(request):
    return render(request,'app1/timoneles.html')

def tripulantes(request):
    return render(request,'app1/tripulantes.html')
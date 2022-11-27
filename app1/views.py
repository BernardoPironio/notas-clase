from django.shortcuts import render
from django.http import HttpResponse
from app1.forms import *
from .models import *

def inicio(request):
    return render(request,'app1/inicio.html')

def entrenadores(request):
    if request.method=="POST":
        form=EntenadorF(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion['nombre']
            apellido=informacion['apellido']
            lancha=informacion['lancha']
            club=informacion['club']
            entrenador=Entrenadores(nombre=nombre,apellido=apellido,lancha=lancha,club=club)
            entrenador.save()
            return render(request, 'app1/inicio.html',{'mensaje':'Entrenador creado correctamente'})
    else:
        formulario=EntenadorF()
    return render(request,'app1/entrenadores.html', {'form':formulario})

def timoneles(request):
    if request.method=='POST':
        form=TimonelesF(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion['nombre']
            apellido=informacion['apellido']
            nombre_barco=informacion['nombre_barco']
            numero_vela=informacion['numero_vela']
            club=informacion['club']
            timonel=Timoneles(nombre=nombre,apellido=apellido,nombre_barco=nombre_barco,numero_vela=numero_vela,club=club)
            timonel.save()
            return render(request, 'app1/inicio.html',{'mensaje':'Timonel creado correctamente'})
    else:
        formulario=TimonelesF()
    return render(request, 'app1/timoneles.html', {'form':formulario})

def tripulantes(request):
    if request.method=='POST':
        form=TripulantesF(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion['nombre']
            apellido=informacion['apellido']
            nombre_barco=informacion['nombre_barco']
            numero_vela=informacion['numero_vela']
            club=informacion['club']
            peso=informacion['peso']
            tripulante=Tripulantes(nombre=nombre,apellido=apellido,nombre_barco=nombre_barco,numero_vela=numero_vela,club=club,peso=peso)
            tripulante.save()
            return render(request, 'app1/inicio.html',{'mensaje':'Tripulante creado correctamente'})
    else:
        formulario=TripulantesF()
    return render(request, 'app1/tripulantes.html', {'form':formulario})

def busquedaentrenadores(request):
    return render(request, 'app1/busquedaentrenadores.html')

def buscar(request):
    if request.GET['lancha']:
        lancha=request.GET['lancha']
        entrenadores=Entrenadores.objects.filter(lancha__icontains=lancha)
        return render(request, 'app1/resultadosbusqueda.html',{'entrenadores':entrenadores})
    else:
        return render(request, 'app1/busquedaentrenadores.html' , {'mensaje':'No ingresaste un numero de lancha'})
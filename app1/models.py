from django.db import models

class Entrenadores(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    lancha=models.IntegerField()
    club=models.CharField(max_length=5)
   
    
class Timoneles(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    nombre_barco=models.CharField(max_length=50)
    numero_vela=models.IntegerField()
    club=models.CharField(max_length=5)

class Tripulantes(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    nombre_barco=models.CharField(max_length=50)
    numero_vela=models.IntegerField()
    club=models.CharField(max_length=5)
    peso=models.FloatField()



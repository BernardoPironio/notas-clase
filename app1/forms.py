from django import forms

class EntenadorF(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    lancha=forms.IntegerField()
    club=forms.CharField(max_length=5)

class TimonelesF(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    nombre_barco=forms.CharField(max_length=50)
    numero_vela=forms.IntegerField()
    club=forms.CharField(max_length=5)

class TripulantesF(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    nombre_barco=forms.CharField(max_length=50)
    numero_vela=forms.IntegerField()
    club=forms.CharField(max_length=5)
    peso=forms.FloatField()


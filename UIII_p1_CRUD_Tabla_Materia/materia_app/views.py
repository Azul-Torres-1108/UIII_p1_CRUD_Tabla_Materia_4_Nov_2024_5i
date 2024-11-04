from django.shortcuts import render
from .models import Materia

def inicio_vista(request):
    lasmaterias=Materia.objects.all()

    return render(request,"gestionarMateria.html")

# Create your views here.

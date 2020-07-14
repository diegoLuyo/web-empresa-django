from django.shortcuts import render

from .models import Servicio

# Create your views here.
def servicios(request):
    servicio= Servicio.objects.all()
    return render(request,"services/services.html", {'servicios':servicio})
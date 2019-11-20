from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Paquete

# Create your views here.

class PaqueteListView(ListView):
    model = Paquete

def destinations(request):
    return render(request,"destinos/destination.html")

def details(request):
    return render(request,"destinos/details.html")
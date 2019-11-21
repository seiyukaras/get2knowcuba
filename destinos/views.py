from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Paquete
from django.views.generic.detail import DetailView


# Create your views here.

class PaqueteListView(ListView):
    model = Paquete
    paginate_by = 8

class PaqueteDetailView(DetailView):
    model = Paquete


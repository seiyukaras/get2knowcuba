from django.shortcuts import render, get_object_or_404
from destinos.models import Paquete

# Create your views here.

def billing(request, slug):
    paquete = get_object_or_404(Paquete, slug=slug)
    return render(request,"billing/form.html", {'paquete': paquete})
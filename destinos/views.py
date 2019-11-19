from django.shortcuts import render

# Create your views here.

def destinations(request):
    return render(request,"destinos/destination.html")

def details(request):
    return render(request,"destinos/details.html")
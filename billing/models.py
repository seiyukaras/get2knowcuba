from django.db import models
from destinos.models import Paquete

# Create your models here.
class billing(models.Model):
    tipo_compania = [("1", "Solo"),("2","Pareja"),("3","Familia")]

    casa_local = models.BooleanField(('Casa Local'), blank=True, null=True)
    hostales = models.BooleanField(('Hostales'), blank=True,null=True)
    hotel = models.BooleanField(('Hotel'), blank=True, null=True)
    compania = models.PositiveSmallIntegerField(choices=tipo_compania)
    adultos = models.PositiveIntegerField(('Adultos'), blank=True, null=True)
    ninos = models.PositiveIntegerField(('Niños'), blank=True, null=True)
    text = models.TextField()
    email = models.EmailField(blank=True, null=True)
    titulo = models.ForeignKey(Paquete, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo.titulo
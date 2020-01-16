from django.db import models
from destinos.models import Paquete

# Create your models here.
class billing(models.Model):
    tipo_compania = [(1, "Solo"),(2,"Pareja"),(3,"Familia")]
    tipo_alojamiento = [(1, "Casa local"),(2,"Hostal"),(3,"Hotel")]

    compania = models.PositiveSmallIntegerField(choices=tipo_compania)
    adultos = models.PositiveIntegerField(('Adultos'), blank=True, null=True)
    ninos = models.PositiveIntegerField(('Niños'), blank=True, null=True)
    alojamiento = models.PositiveSmallIntegerField(choices=tipo_alojamiento)
    text = models.TextField()
    email = models.EmailField(blank=True, null=True)
    titulo = models.ForeignKey(Paquete, on_delete=models.CASCADE)
    comprobante_presupuesto = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ['titulo']

    def __str__(self):
        return self.titulo.titulo
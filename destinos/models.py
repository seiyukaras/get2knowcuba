from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Paquete(models.Model):
    titulo = models.CharField(max_length=200)
    destinos = models.CharField(max_length=500, blank=False)
    contenido = RichTextField()
    duracion = models.PositiveSmallIntegerField()
    precio = models.PositiveIntegerField()
    fotos_portada = models.FileField(upload_to='img/')
    slug = models.SlugField(max_length=40)
    guia = models.BooleanField(('Guide'), blank=True, null=True)
    chofer = models.BooleanField(('Driver'), blank=True,null=True)
    traslado = models.BooleanField(('Airport transfer'), blank=True, null=True)
    home = models.BooleanField(default=False)
    round = models.BooleanField(default=False)
    oferta = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
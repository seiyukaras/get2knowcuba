from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class ServiciosInlcuidos(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name="Servicio incluido"
        verbose_name_plural="Servicios incluidos"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class ServiciosNoInlcuidos(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name="Servicio No incluido"
        verbose_name_plural="Servicios No incluidos"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


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
    servicios = models.ManyToManyField(ServiciosInlcuidos, verbose_name="Servicios Inlcuidos", related_name="get_services")
    noservicios = models.ManyToManyField(ServiciosNoInlcuidos, verbose_name="Servicios No Inlcuidos", related_name="get_not_services")

    def __str__(self):
        return self.titulo


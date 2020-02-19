from django.contrib import admin

# Register your models here.
from .models import Paquete, ServiciosInlcuidos, ServiciosNoInlcuidos

class PaqueteAdmin(admin.ModelAdmin):
     prepopulated_fields = { 'slug': ['titulo']}

admin.site.register(Paquete, PaqueteAdmin)
admin.site.register(ServiciosInlcuidos)
admin.site.register(ServiciosNoInlcuidos)
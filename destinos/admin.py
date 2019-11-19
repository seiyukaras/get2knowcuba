from django.contrib import admin

# Register your models here.
from .models import Paquete

class PaqueteAdmin(admin.ModelAdmin):
     prepopulated_fields = { 'slug': ['titulo']}

admin.site.register(Paquete, PaqueteAdmin)
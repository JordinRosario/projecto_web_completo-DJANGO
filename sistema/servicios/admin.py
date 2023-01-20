from django.contrib import admin
from .models import Servicios
# Register your models here.

class ServiciosAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'actualizacion')

admin.site.register(Servicios, ServiciosAdmin)

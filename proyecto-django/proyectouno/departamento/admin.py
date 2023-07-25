from django.contrib import admin

from departamento.models import *

class EdificioAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'direccion', 'ciudad', 'tipo')
    search_fields = ('nombre', 'direccion')

admin.site.register(Edificio, EdificioAdmin)

class PropietarioAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'apellido', 'cedula')
    search_fields = ('nombre', 'cedula')
    

admin.site.register(Propietario, PropietarioAdmin)

class DepartamentoAdmin(admin.ModelAdmin):

    list_display = ('costo', 'numero_cuartos', 'edificio', 'propietario')

    raw_id_fields = ('edificio', 'propietario')

admin.site.register(Departamento, DepartamentoAdmin)


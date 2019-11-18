from django.contrib import admin
from .models import Persona, DirOrigen, DirDestino

# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'run','correo')
    search_fields = ('nombre', 'nombre')


admin.site.register(Persona,PersonaAdmin)
admin.site.register(DirOrigen)
admin.site.register(DirDestino)
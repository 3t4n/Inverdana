from django.contrib.admin import ModelAdmin
from .models import *
from users.models import *

class QrCodeAdmin(ModelAdmin):
    model = Identifier.QRcode
    exclude = ['string']
    list_display = ('string', 'status')
    list_filter = ('status',)
#    add_form_template='admin/qrcodes/add.html'

class TreeAdmin(ModelAdmin):
    model = Tree.Tree
    list_display=('nombre','edad','especie')
    list_filter = ('age','specie_id')
    search_fields =('name',)
    def edad(self,obj):
        return obj.age
    edad.short_description = "Edad"
    def nombre(self,obj):
        return obj.name
    nombre.short_description = "Nombre"
    def especie(self,obj):
        return obj.specie_id
    especie.short_description = "Especie"
        
class EventAdmin(ModelAdmin):
    model=Event.Event
    search_fields =('name',)
    list_display=('nombre','info','inicio','final')
    list_filter = ('initial_date','final_date')
    def nombre(self,obj):
        return obj.name
    nombre.short_description = "Nombre del evento"
    def info(self,obj):
        return obj.info
    info.short_description ="Información"
    def inicio(self,obj):
        return obj.initial_date
    inicio.short_description = "Fecha de inicio"
    def final(self,obj):
        return obj.final_date
    final.short_description = "Fecha de final"

class SuggestionAdmin(ModelAdmin ):
    model=Suggestions.Suggestion
    list_display=('titulo','descripcion')
    list_filter = ('seen','dateCreated')
    list_per_page = 5
    def titulo(self,obj):
        return obj.title
    titulo.short_description = "Título"
    def descripcion(self,obj):
        return obj.description
    descripcion.short_description = "Descripcion"
    def visto(self,obj):
        return obj.seen
    visto.short_description = "Visto"

class OrganizationAdmin(ModelAdmin):
    list_per_page = 5
    list_display = ('nombre','numero')
    def nombre(self,obj):
        return obj.name
    nombre.short_description = "Nombre"
    def numero(self,obj):
        return obj.numero
    numero.short_description = "Numero"


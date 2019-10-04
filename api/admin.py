from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Contact.Contact)
admin.site.register(WorldBorder.WorldBorder)
admin.site.register(GeoEntity.GeoEntity)
admin.site.register(Preference.Preference)
admin.site.register(Tree.Tree)
admin.site.register(Tree.TreeSpecie)
admin.site.register(Tree.Share)

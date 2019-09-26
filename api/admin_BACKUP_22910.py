from django.contrib import admin
<<<<<<< HEAD
from .models import Contact, Country, GeoEntity, Preference
=======
from .models import *
>>>>>>> javier/TreeModule
# Register your models here.
admin.site.register(Contact.Contact)
admin.site.register(Country.Country)
admin.site.register(GeoEntity.GeoEntity)
<<<<<<< HEAD
admin.site.register(Preference.Preference)
=======
admin.site.register(Tree.Tree)
admin.site.register(Tree.TreeSpecie)
admin.site.register(Tree.Share)
>>>>>>> javier/TreeModule

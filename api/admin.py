from django.contrib import admin
from .models import Contact, Country, GeoEntity, Preference
# Register your models here.
admin.site.register(Contact.Contact)
admin.site.register(Country.Country)
admin.site.register(GeoEntity.GeoEntity)
admin.site.register(Preference.Preference)

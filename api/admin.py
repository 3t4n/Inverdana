from django.contrib import admin
from .models import Contact
from .models import Country
# Register your models here.
admin.site.register(Contact.Contact)
admin.site.register(Country.Country)

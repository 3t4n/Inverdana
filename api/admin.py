from .forms.admin.login import *
from django.contrib.admin import AdminSite
from .models import *
from django.contrib.auth.models import User
class AdminSite(AdminSite):
    site_header = 'Inverdana'
    login_template ='admin/login.html'
    login_form = AuthForm
admin = AdminSite(name='Inverdana')

# Register your models here.
admin.register(Contact.Contact)
admin.register(WorldBorder.WorldBorder)
admin.register(Preference.Preference)
admin.register(Tree.Tree)
admin.register(Tree.TreeSpecie)
admin.register(Tree.Share)
admin.register(Photo.Photo)
admin.register(Identifier.QRcode)
admin.register(User)

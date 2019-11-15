from django.contrib.admin import ModelAdmin
from .models import *

class QrCodeAdmin(ModelAdmin):
    model = Identifier.QRcode
    exclude = ['string']
    add_form_template='admin/qrcodes/add.html'

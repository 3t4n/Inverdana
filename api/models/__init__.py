from django.db.models.signals import pre_save,post_init
from . import Contact,WorldBorder,Preference,GeoEntity,Tree,Photo,Identifier,Stock
from users.models import *
from django.utils.crypto import get_random_string
from django.conf import settings as appsettings
import qrcode

##Receiver function

def QRcode_receiver(sender, instance, *args, **kwargs):
    if not instance.string:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,)
        instance.string = get_random_string(length=6)
        qr.add_data(instance.string)
        img = qr.make_image()
        codepwd = appsettings.MEDIA_ROOT+"qr/"+instance.string+".png"
        img.save(codepwd)
        instance.code = "qr/"+instance.string+".png"

def Suggestions_receiver(sender,instance,*args,**kwargs):
    if not instance.seen:
        if instance.id:
            instance.seen = True
            print("lol")
            instance.seen = True
            instance.save(force_update=True)
        
post_init.connect(Suggestions_receiver, sender=Suggestions.Suggestion)
pre_save.connect(QRcode_receiver, sender=Identifier.QRcode)

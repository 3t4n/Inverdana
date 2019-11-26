from django.db.models.signals import pre_save
from . import Contact,WorldBorder,Preference,GeoEntity,Tree,Photo,Identifier, Event,Suggestions,Feed,Stock
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

pre_save.connect(QRcode_receiver, sender=Identifier.QRcode)

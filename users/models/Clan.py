from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models as geomodels
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Clan(models.Model):
    name = models.CharField(max_length=300, blank=False)
    info = models.TextField(max_length=300, blank=False)
    photo = models.ImageField(upload_to='clans', null=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    photo_thumbnail = ImageSpecField(source='photo',
                                     processors=[ResizeToFill(250, 250)],
                                     format='JPEG',
                                     options={'quality': 60})

    class Meta:
        verbose_name_plural = "Clans"
        verbose_name="Clan"

    def __str__(self):
        return '%s' % (self.name)

class MemberShip(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="Personas",related_name="clans")
    clan_id = models.ForeignKey(Clan, on_delete=models.CASCADE, verbose_name="Clan")
    date_joined = models.DateField(auto_now_add=True)
    invite_reason = models.CharField(max_length=64)
    
    class Meta:
        verbose_name_plural = "Membresías"
        verbose_name="Membresía"
    def __str__(self):
        return '%s' % (self.name)

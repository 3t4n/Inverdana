from django.db import models
from django.contrib.auth.models import User
from . import WorldBorder,Achievement
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Contact(models.Model):
    cellphone=models.CharField(max_length=50)
    birthday = models.DateField(null=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True, related_name='info')
    """If for some reason one country is removed then all Contact go to NULL"""
    country = models.ForeignKey(WorldBorder.WorldBorder, on_delete=models.SET_NULL, null=True, related_name='country')
    photo = models.ImageField(upload_to='users', null=True)
    photo_thumbnail = ImageSpecField(source='photo',
                                     processors=[ResizeToFill(250, 250)],
                                     format='JPEG',
                                     options={'quality': 60})

    class Meta:
        verbose_name_plural = "Fichas de Contacto" 
    def __str__(self):
        return '%s' % (self.user_id)

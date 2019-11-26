from django.db import models
from django.contrib.auth.models import User
from . import Contact
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class AchievementCatalog(models.Model):
    name = models.CharField(max_length=50,verbose_name="Nombre")
    desc = models.TextField(max_length=255,verbose_name="Descripción")
    photo = models.ImageField(upload_to='trees',verbose_name="Foto")
    photo_thumbnail = ImageSpecField(source='photo',
                                      processors=[ResizeToFill(250, 250)],
                                      format='JPEG',
                                      options={'quality': 60})
    achievement = models.ManyToManyField(User, through='Achievement')
    class Meta:
        verbose_name_plural = "Catalogo de  Logros"
        verbose_name="logro"
    def __str__(self):
        return '%s' % (self.name)

class Achievement(models.Model):
    dateCreated = models.DateField(auto_now_add=True)
    user_id  = models.ForeignKey(User, on_delete=models.CASCADE, related_name='achievements',verbose_name="Usuario")
    achievement_id = models.ForeignKey(AchievementCatalog, on_delete=models.CASCADE, related_name='nameA',verbose_name="Logro")
    
    class Meta:
        verbose_name_plural = "Logros"
        verbose_name="logro"
   

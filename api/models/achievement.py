from django.db import models
from django.contrib.auth.models import User
from . import Contact


class AchievementCatalog(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='trees')
    photo_thumbnail = ImageSpecField(source='photo',
                                      processors=[ResizeToFill(250, 250)],
                                      format='JPEG',
                                      options={'quality': 60})
    class Meta:
        verbose_name_plural = "Catalogo de  Logros"
        verbose_name="logro"
    def __str__(self):
        return '%s' % (self.tree_id)


class Achievement(models.Model):
    dateCreated = models.DateField(auto_now_add=True)

from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models as geomodels
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    info = models.TextField(max_length=300, blank=False)
    photo = models.ImageField(upload_to='posts')
    photo_thumbnail = ImageSpecField(source='photo',
                                     processors=[ResizeToFill(250, 250)],
                                     format='JPEG',
                                     options={'quality': 60})

    class Meta:
        verbose_name_plural = "Posts"
        verbose_name="Post"

    def __str__(self):
        return '%s: %s' % (self.user, self.info)



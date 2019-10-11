from django.db import models
from django.contrib.auth import authenticate, get_user_model
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from . import Tree

User = get_user_model()

class Photo(models.Model):
    photo = models.ImageField(upload_to='trees')
    photo_thumbnail = ImageSpecField(source='photo',
                                      processors=[ResizeToFill(250, 250)],
                                      format='JPEG',
                                      options={'quality': 60})
    treed_id = models.ForeignKey(Tree.Tree, on_delete=models.SET_NULL, null=True,related_name='photos')

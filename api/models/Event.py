from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models as geomodels
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Event(models.Model):
    name = models.CharField(max_length=100, blank=False)
    info = models.TextField(max_length=300, blank=False)
    size = models.IntegerField(default=0)
    initial_date = models.DateTimeField(verbose_name="Fecha de Inicio")
    final_date = models.DateTimeField(verbose_name="Fecha de Final")
    place = geomodels.PointField()
    photo = models.ImageField(upload_to='events')
    photo_thumbnail = ImageSpecField(source='photo',
                                     processors=[ResizeToFill(250, 250)],
                                     format='JPEG',
                                     options={'quality': 60})
    class Meta:
        verbose_name_plural = "Eventos"
        verbose_name="Evento"
    def __str__(self):
        return '%s, Participantes: %s' % (self.name, self.size)



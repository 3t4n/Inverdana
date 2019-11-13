from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models as geomodels
import datetime

class Event(models.Model):
    name = models.CharField(max_length=100, blank=False)
    info = models.TextField(max_length=300, blank=False)
    size = models.IntegerField(default=0)
    #date = models.DateField(("Date"), default=datetime.date.today)
    place = geomodels.PointField()
    class Meta:
        verbose_name_plural = "Eventos"
        verbose_name="Evento"
    def __str__(self):
        return '%s, Participantes: %s' % (self.name, self.size)



from django.db import models
from django.contrib.gis.db import models as geomodels
class GeoEntity(models.Model):
    name = models.CharField(max_length=100, blank=False)
    geometry = geomodels.PointField()

from django.db import models
from django.contrib.gis.db import models as geomodels

class Tree(models.Model):
    species = models.ForeignKey(TreeSpecies, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100, blank=False)
    age = models.IntegerField(default=0)
    point = geomodels.PointField()

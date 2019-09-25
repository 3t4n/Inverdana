from django.db import models
import TreeSpecie
import Share
from django.contrib.gis.db import models as geomodels

class Tree(models.Model):
    specie_id = models.ForeignKey(TreeSpecie, on_delete=models.SET_NULL)
    share_id = models.OneToOneField(Share, on_delete=models.SET_NULL, primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    age = models.IntegerField(default=0)
    point = geomodels.PointField()

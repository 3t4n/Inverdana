#from django.db import models
from django.contrib.gis.db import models


"""Country class with django.contrib.gis.db.models.Model
   It will use to determinate what country is certain Point
   Based on https://docs.djangoproject.com/en/2.2/ref/contrib/gis/tutorial/#setting-up"""


class Country(models.Model):
    """Non GIS attributes"""
    name = models.CharField(max_length=50)
    area = models.IntegerField(default=0)
    fips = models.CharField('FIPS Code', max_length=2, default='XX')
    iso2 = models.CharField('2 Digit ISO', max_length=2, default='XX')
    iso_3 = models.CharField('3 Digit ISO', max_length=3, default='XX')
    un = models.IntegerField('United Nations Code', default=-1)
    region = models.IntegerField('Region Code', default=-1)
    subregion = models.IntegerField('Sub-Region Code', default=-1)
    """GIS Attributes"""
    location = models.PointField(null=True)
    mpoly = models.MultiPolygonField(null=True)

    """For Admin and API"""
    def __str__(self):
        return self.name

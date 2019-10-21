from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models as geomodels

class TreeSpecie(models.Model):
    commonname = models.CharField(max_length=100, blank=False)
    sciname = models.CharField(max_length=100, blank=False)
    class Meta:
        verbose_name_plural = "Especies de árboles"
        verbose_name="especie de árbol"


class Tree(models.Model):
    specie_id = models.ForeignKey(TreeSpecie, on_delete=models.SET_NULL, null=True)
    shareholders = models.ManyToManyField(User, through='Share')
    name = models.CharField(max_length=100, blank=False)
    age = models.IntegerField(default=0)
    point = geomodels.PointField()
    class Meta:
        verbose_name_plural = "Árboles"
        verbose_name="árbol"

class Share(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shares')
    tree = models.ForeignKey(Tree, on_delete=models.SET_NULL, null=True)
    owner = models.BooleanField(default=True)
    percentage = models.IntegerField(default=100)
    dateCreated = models.DateField(auto_now_add=True)
    dateModified = models.DateField(auto_now=True)
    class Meta:
        verbose_name_plural = "Acciones"
        verbose_name = "acción"

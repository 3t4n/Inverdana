from django.bd import models

class TreeSpecies(models.Model):
    commonname = models.CharField(max_length=100, blank=False)
    sciname = models.CharField(max_length=100, blank=False)
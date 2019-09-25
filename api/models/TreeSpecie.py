from django.db import models

class TreeSpecie(models.Model):
    commonname = models.CharField(max_length=100, blank=False)
    sciname = models.CharField(max_length=100, blank=False)
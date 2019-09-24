from django.db import models

class Shares(models.Model):
    user_id = models.ForeignKey(TreeSpecies, on_delete=models.SET_NULL)
    owner = models.BooleanField(default=False)
    percentage
    dateCreated
    dateModified
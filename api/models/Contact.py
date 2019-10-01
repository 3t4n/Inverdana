from django.db import models
from django.contrib.auth.models import User
from . import WorldBorder

class Contact(models.Model):
    address1=models.CharField(max_length=50);
    address2=models.CharField(max_length=50);
    cellphone=models.CharField(max_length=50);
    user_id = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True, related_name='info')
    """If for some reason one country is removed then all Contact go to NULL"""
    country = models.OneToOneField(WorldBorder.WorldBorder, on_delete=models.SET_NULL, null=True, related_name='country')

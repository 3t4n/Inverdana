from django.db import models
from django.contrib.auth.models import User
from . import WorldBorder,Achievement

class Contact(models.Model):
    cellphone=models.CharField(max_length=50)
    birthday = models.DateField(null=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True, related_name='info')
    """If for some reason one country is removed then all Contact go to NULL"""
    country = models.ForeignKey(WorldBorder.WorldBorder, on_delete=models.SET_NULL, null=True, related_name='country')
    class Meta:
        verbose_name_plural = "Fichas de Contacto" 
    def __str__(self):
        return '%s' % (self.user_id)

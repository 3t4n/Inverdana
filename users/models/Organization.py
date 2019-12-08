from django.db import models
from django.contrib.auth.models import User

class Organization(models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name="Nombre Organización")
    info = models.TextField(max_length=900, blank=False, verbose_name="Descripción")
    legalrep = models.CharField(max_length=100, verbose_name="Representante")
    number = models.CharField(max_length=100, verbose_name="Número de teléfono")
    class Meta:
        verbose_name_plural = "Organizaciones"
        verbose_name="Organización"
    def __str__(self):
        return 'Organización: %s' % (self.name)



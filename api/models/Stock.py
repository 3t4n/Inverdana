from django.db import models
from django.contrib.auth.models import User
from api.models.Tree import TreeSpecie



class Stock(models.Model):
    specie_id = models.ForeignKey(TreeSpecie, on_delete=models.SET_NULL, null=True, verbose_name="Especie")
    name = models.CharField(max_length=100, blank=False, verbose_name="Nombre")
    age = models.IntegerField(default=0, verbose_name="Edad")

    class Meta:
        verbose_name_plural = "Árboles de Inverdana (Inventario)"
        verbose_name = "árbol"

    def __str__(self):
        return 'Nombre: %s, Especie: %s' % (self.name, self.specie_id)



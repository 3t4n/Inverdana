from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class PineSpecie(models.Model):
    specie_id = models.CharField(max_length=100, null=True, verbose_name='Especie')
    sciname = models.CharField(max_length=100, blank=False, verbose_name='nombre científico')

    class Meta:
        verbose_name_plural = "Especies de árboles de navidad"
        verbose_name = "especie de árbol de navidad"

    def __str__(self):
        return '%s' % (self.specie_id)

class PineState(models.Model):
    name = models.CharField(max_length=100, blank=False, null=True, verbose_name='estatus del árbol')

    class Meta:
        verbose_name_plural = "Estados de árboles de navidad"
        verbose_name = "estado del árbol de navidad"

    def __str__(self):
        return '%s' % (self.name)

class PineSize(models.Model):
    size = models.CharField(max_length=50, blank=False,verbose_name="Tamaño")

    class Meta:
        verbose_name_plural = "Tamaños de árboles de navidad"
        verbose_name = "tamaño"

    def __str__(self):
        return '%s' % (self.size)

class PineTree(models.Model):
    specie_id = models.ForeignKey(PineSpecie, on_delete=models.SET_NULL, null=True, verbose_name="Especie")
    state = models.ForeignKey(PineState, on_delete=models.SET_NULL, null=True, verbose_name="Estado")
    size = models.ForeignKey(PineSize, on_delete=models.SET_NULL, null=True, verbose_name="Tamaño")
    class Meta:
        verbose_name_plural = "Árboles de Navidad"
        verbose_name = "árbol de navidad"

class PineLoan(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tree_id = models.ForeignKey(PineTree, on_delete=models.SET_NULL, null=True, verbose_name="Arbol")
    location = models.TextField(max_length=100, blank=False)
    price = models.IntegerField(null=True, blank=False,verbose_name="Precio")

    class Meta:
        verbose_name_plural = "Préstamos"
        verbose_name = "préstamo"

    def __str__(self):
        return 'Nombre: %s, Especie: %s' % (self.user_id, self.location)


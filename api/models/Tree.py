from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models as geomodels
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class TreeSpecie(models.Model):
    commonname = models.CharField(max_length=100, blank=False)
    sciname = models.CharField(max_length=100, blank=False)
    
    class Meta:
        verbose_name_plural = "Especies de árboles"
        verbose_name="especie de árbol"
    def __str__(self):
        return '%s' % (self.commonname)

class TreeTip(models.Model):
    title = models.CharField(max_length=255, blank=False)
    tip = models.TextField(max_length=255, blank=False)
    tree_id = models.ForeignKey(TreeSpecie,on_delete=models.CASCADE, related_name="tips")
    def __str__(self):
        return '%s %s' % (self.title,self.tree_id)
    class Meta:
        verbose_name_plural = "Tips de árboles"
        verbose_name="tip"

class TreeState(models.Model):
    name = models.CharField(max_length=100, blank=False)
    class Meta:
        verbose_name_plural = "Estados catálogo"
        verbose_name="estado"
    def __str__(self):
        return '%s' % (self.name)

class Tree(models.Model):
    specie_id = models.ForeignKey(TreeSpecie, on_delete=models.SET_NULL, null=True, verbose_name="Especie")
    shareholders = models.ManyToManyField(User, through='Share')
    state = models.ManyToManyField(TreeState, through='HasState')
    name = models.CharField(max_length=100, blank=False)
    age = models.IntegerField(default=0, verbose_name="Edad")
    point = geomodels.PointField()
    class Meta:
        verbose_name_plural = "Árboles de usuarios"
        verbose_name="árbol de usuario"
    
    def x(self):
        return self.point.x
    
    def y(self):
        return self.point.y
    def __str__(self):
        return 'Nombre: %s, Especie: %s' % (self.name, self.specie_id)

class HasState(models.Model):
    tree = models.ForeignKey(Tree, on_delete=models.SET_NULL, null=True, related_name="states")
    state = models.ForeignKey(TreeState, on_delete=models.SET_NULL, null=True)
    photo = models.ImageField(upload_to='reports', null=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=300, blank=False, null=True)
    photo_thumbnail = ImageSpecField(source='photo',
                                     processors=[ResizeToFill(250, 250)],
                                     format='JPEG',
                                     options={'quality': 60})
    class Meta:
        verbose_name_plural = "Estados"
        verbose_name="estado"
    def __str__(self):
        return ' %s , Estado %s' % ( self.tree,self.state)
    #Photos

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

    def __str__(self):
        return '%s %s' % (self.tree, self.owner)

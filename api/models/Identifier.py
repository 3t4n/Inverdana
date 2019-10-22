from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.auth import authenticate, get_user_model
from django.conf import settings
from . import Tree
#Abstract class for auth
class Identifier(models.Model):
    status = models.CharField(max_length=3, choices=settings.IDENTIFIER_STATUS, default='NA')
    tree_id = models.ForeignKey(Tree.Tree,on_delete=models.SET_NULL,null=True,related_name='identifiers',blank=True)
    class Meta:
        abstract = True

    def __str__(self):
        return '%s' % (self.status)

class QRcode(Identifier):
    string = models.CharField(max_length=6,blank=True,primary_key=True)
    code = models.ImageField(upload_to='qr', blank=True, null=True)

    def __str__(self):
        return 'QR= %s' % (self.string)
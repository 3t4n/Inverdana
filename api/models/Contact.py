from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    address1=models.CharField(max_length=50);
    address2=models.CharField(max_length=50);
    cellphone=models.CharField(max_length=50);
    user_id = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    #Country

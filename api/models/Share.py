from django.db import models
from django.contrib.auth.models import User
import datetime

class Share(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    owner = models.BooleanField(default=True)
    percentage = models.IntegerField(default=0)
    dateCreated = models.DateField(auto_now_add=True)
    dateModified = models.DateField(auto_now_add=True)
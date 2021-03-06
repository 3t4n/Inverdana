from django.db import models
from django.contrib.auth.models import User
"""
Preferences module
"""

class Preference(models.Model):
    #Subcription in order to be implemented in Sprint2
    #Local Lang to be implemented in Sprint3
    #Local Lang to be implemented in Sprint3
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,related_name="preferences")
    push_notifications_trees = models.BooleanField(default=True)
    push_notifications_events = models.BooleanField(default=True)

from django.db import models
from django.contrib.auth.models import User


class PushToken(models.Model):
    token = models.CharField(max_length=50)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE, related_name='push_tokens')
    class Meta:
        verbose_name_plural = "Push Tokens" 
    def __str__(self):
        return '%s' % (self.token)

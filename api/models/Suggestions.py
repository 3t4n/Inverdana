from django.db import models


class Suggestion(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=300, blank=False)
    seen = models.BooleanField(default=False)
    dateCreated = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Sugerencias"
        verbose_name="Sugerencia"


    def __str__(self):
        return '%s' % self.title

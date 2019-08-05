from django.db import models
from datetime import datetime
from django.utils import timezone
from django.template import defaultfilters

# Listed here are the models that aid us in saving and storing information.
class Table(models.Model):
    table = models.CharField(max_length=50)
    def __str__(self):
        return self.table
    class Meta:
        verbose_name_plural = "Tables"

class Taste(models.Model):
    taste_name = models.CharField(max_length=50)
    def __str__(self):
        return self.taste_name
    class Meta:
        verbose_name_plural = "Tastes"

class Vote(models.Model):
    vote_value = models.IntegerField()
    voted_at = models.DateTimeField(default=timezone.now(), blank=True)
    current_value = models.IntegerField()
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    taste = models.ForeignKey(Taste, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.voted_at)
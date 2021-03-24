from django.db import models

from django.db import models
from django.db.models.base import Model

class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    weapon = models.CharField(max_length=60,default="sword")

    def __str__(self):
        return self.name

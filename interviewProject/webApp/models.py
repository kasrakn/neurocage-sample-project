from django.db import models

# Create your models here.

class Cage(models.Model):
    label = models.CharField(max_length=255)
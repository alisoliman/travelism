from django.db import models


# Create your models here.

class Agency(models.Model):
    name = models.CharField(max_length=128)
    brief = models.TextField()


class Destination(models.Model):
    name = models.CharField(max_length=128)

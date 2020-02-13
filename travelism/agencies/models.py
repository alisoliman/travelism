from django.db import models


# Create your models here.

class Agency(models.Model):
    name = models.CharField(max_length=128)
    brief = models.TextField()
    cover_picture = models.ImageField()
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.name

from django.db import models


class Trip(models.Model):
    title = models.CharField(max_length=256)
    price = models.FloatField(default=0)
    start_date = models.DateField()
    end_date = models.DateField()
    requirements = models.TextField()
    payment_methods = models.TextField()

    def __str__(self):
        return self.title

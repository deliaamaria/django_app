from django.db import models

class App(models.Model):
    AppName = models.CharField(max_length=1000)
    Category = models.CharField(max_length=1000)
    Rating = models.FloatField()
    MaximumInstalls = models.DecimalField(decimal_places=0, max_digits=1000)
    Price = models.FloatField()
    Released = models.DateField()


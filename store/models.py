from django.db import models

# Create your models here.

class Stores(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    postal_code = models.IntegerField()

    def __str__(self):
        return self.name
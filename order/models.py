from django.db import models

# Create your models here.

class Order(models.Model):
    client = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cliente: {self.client} - Producto {self.product} - Creation Time {self.creation_time}"


from django.db import models

# Create your models here.

class Product(models.Model):
    item = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField()


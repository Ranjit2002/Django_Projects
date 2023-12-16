from django.db import models

# Create your models here.


class Store(models.Model):
    customer = models.CharField(max_length=50)
    product = models.CharField(max_length=100)
    date = models.DateTimeField()
    price = models.IntegerField()

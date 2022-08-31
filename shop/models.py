from django.db import models
from datetime import datetime


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    # price = models.IntegerField()
    # discount = models.FloatField()
    # discount_price = models.FloatField()
    # size = models.CharField(max_length=20)
    # light = models.CharField(max_length=20)
    # care = models.CharField(max_length=20)
    # selected_item = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    # is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name



from django.db import models
from datetime import datetime


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.FloatField(default=0)
    # Assigning 'discount_percent' a default value of 0 so it doesn't throw a 'NoneType' error when it's null.
    discount_percent = models.FloatField(default=0)
    size = models.CharField(max_length=20, blank=True)
    light = models.CharField(max_length=20, blank=True)
    care = models.CharField(max_length=20, blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    @property
    def discount(self):
        if self.discount_percent > 0:
            discounted_price = self.price - self.price * self.discount_percent / 100
            return discounted_price

    def __str__(self):
        return self.name


# class OrderItem(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
#     #order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
#     quantity = models.IntegerField(default=0, null=True, blank=True)

#     # get_total function has to be updated too to calculate using the correct current price

#     @property
#     def get_total(self):
#         if self.product.discount_percent > 0:
#             price_now = self.product.price - self.product.price * \
#                 self.product.discount_percent / 100
#         else:
#             price_now = self.product.price

#         total = price_now * self.quantity
#         return total

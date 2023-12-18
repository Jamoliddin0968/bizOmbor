from datetime import datetime

from django.db import models


def get_current_date_as_integer():
    current_date = datetime.now()
    return int(current_date)
class Sale(models.Model):
    date = models.IntegerField(default=get_current_date_as_integer)
    discount = models.IntegerField()
    cash = models.IntegerField()
    without_cash = models.IntegerField()
    total_summa = models.IntegerField()



class SaleItem(models.Model):
    sale = models.ForeignKey('sales.sale',related_name='sale_items',on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product',on_delete=models.CASCADE)
    price = models.IntegerField()
    amount = models.FloatField(default=0)
    total = models.IntegerField()

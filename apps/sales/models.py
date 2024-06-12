from django.db import models


class Sale(models.Model):
    smena = models.ForeignKey('smenas.smena', on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    discount = models.IntegerField(default=0)
    cash = models.IntegerField(default=0)
    without_cash = models.IntegerField(default=0)
    total_summa = models.IntegerField(default=0)
    store = models.ForeignKey('stores.Store', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)


class SaleItem(models.Model):
    sale = models.ForeignKey('sales.sale', related_name='sale_items', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    price = models.IntegerField()
    amount = models.FloatField(default=0)
    total = models.IntegerField()

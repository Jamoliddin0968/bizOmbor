from django.db import models

from apps.tools.utils import get_current_date_as_integer


# Create your models here.
class Recovery(models.Model):
    sale = models.ForeignKey('sales.sale',related_name='sale_recovery',on_delete=models.CASCADE)
    date = models.IntegerField(default=get_current_date_as_integer)
    total_summa = models.IntegerField(default=0)
    user = models.ForeignKey('users.User',on_delete=models.CASCADE)

class RecoveryItem(models.Model):
    recovery = models.ForeignKey(Recovery, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('products.Product',on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
from django.db import models


# Create your models here.
class Recovery(models.Model):
    sale = models.OneToOneField('sales.sale', related_name='sale_recovery', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    total_summa = models.IntegerField(default=0)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    smena = models.ForeignKey('smenas.smena', on_delete=models.SET_NULL, null=True, blank=True)


class RecoveryItem(models.Model):
    recovery = models.ForeignKey(Recovery, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    amount = models.FloatField(default=0)

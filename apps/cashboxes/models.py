from django.db import models

# Create your models here.
class Cashbox(models.Model):
    store = models.ForeignKey('stores.Store',on_delete=models.CASCADE)
    expire_date = models.IntegerField()
    device_id = models.CharField(max_length=31)
    device_name = models.CharField(max_length=31)
    is_active = models.BooleanField(default=False)


class Session(models.Model):
    start_date = models.IntegerField()
    end_date = models.IntegerField()

class CashboxPermission(models.Model):
    user = models.ForeignKey('users.User',on_delete=models.CASCADE)
    cashbox = models.ForeignKey('cashboxes.cashbox',on_delete=models.CASCADE)
    session = models.ForeignKey('cashboxes.session',on_delete=models.CASCADE)


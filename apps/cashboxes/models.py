from django.db import models
# Create your models here.
class CashBox(models.Model):
    user = models.OneToOneField('users.User',on_delete=models.CASCADE)
    store = models.ForeignKey('stores.Store',on_delete=models.CASCADE)
    start_date = models.IntegerField()
    end_date = models.IntegerField()
    is_active = models.BooleanField(default=False)




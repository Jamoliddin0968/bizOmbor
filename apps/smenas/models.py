from django.db import models


class Smena(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, related_name='Ishchi', null=True, blank=True)
    store = models.ForeignKey('stores.Store', on_delete=models.CASCADE, related_name="Dokon")
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    cash = models.IntegerField(default=0)

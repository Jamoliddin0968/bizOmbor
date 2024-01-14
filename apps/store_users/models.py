from django.db import models


class StoreUser(models.Model):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE, unique=True)
    store = models.ForeignKey('stores.Store', on_delete=models.CASCADE)

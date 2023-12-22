from django.db import models
from apps.users.models import Manager
class Store(models.Model):
    name = models.CharField(max_length=127)
    address = models.CharField(max_length=255)


    manager = models.ForeignKey('users.Manager',on_delete=models.CASCADE,limit_choices_to={'is_manager': True})

class StoreUser(models.Model):
    user=models.OneToOneField('users.User',on_delete=models.CASCADE)


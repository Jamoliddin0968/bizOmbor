from django.db import models

from apps.users.models import User

class StoreUser(User):
    store = models.ForeignKey('stores.Store', on_delete=models.CASCADE)

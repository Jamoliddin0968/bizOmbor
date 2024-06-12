from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=127)
    address = models.CharField(max_length=255)
    manager = models.ForeignKey('users.User', on_delete=models.CASCADE,related_name="user_stores")

    def __str__(self):
        return f"{self.manager.username} {self.name}"

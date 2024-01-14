from django.db import models

# Create your models here.
class Tarif(models.Model):
    name = models.CharField(max_length=127)
    store_count = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name

from django.db import models

class Category(models.Model):
    name= models.CharField(max_length=63)
    image = models.ImageField()
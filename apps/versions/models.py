from django.db import models

class Version(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=255,default="product_add")
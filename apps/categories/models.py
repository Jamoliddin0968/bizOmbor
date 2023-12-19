import os
import uuid

from django.db import models

def _generate_filename(instance, filename):
    file_extension = os.path.splitext(filename)[1]
    uuid_filename = f"{uuid.uuid4()}{file_extension}"
    return os.path.join('images/categories/', uuid_filename)
class Category(models.Model):
    name= models.CharField(max_length=63)
    image = models.ImageField(upload_to=_generate_filename,null=True,blank=True)
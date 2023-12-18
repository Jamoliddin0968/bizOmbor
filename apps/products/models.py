import uuid
import os
from django.db import models

MEASURE_TYPES = (
    ('kg','kg'),
    ('litr','litr'),
    ('dona','dona'),
    ('gr','gr'),
    ('metr','metr'),
)



def _generate_filename(instance, filename):
    file_extension = os.path.splitext(filename)[1]
    uuid_filename = f"{uuid.uuid4()}{file_extension}"
    return os.path.join('images/products/', uuid_filename)

class Product(models.Model):
    category = models.ForeignKey('categories.Category',on_delete=models.CASCADE)
    name = models.CharField(max_length=127)
    description = models.TextField()
    measure = models.CharField(choices=MEASURE_TYPES,max_length=15)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to=_generate_filename)
    barcode = models.CharField(max_length=31)
    barcode_type = models.CharField(max_length=31)



import os
import uuid

from django.db import models
from faker import Faker
MEASURE_TYPES = (
    ('kg', 'kg'),
    ('litr', 'litr'),
    ('dona', 'dona'),
    ('gr', 'gr'),
    ('metr', 'metr'),
)
fake = Faker()
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.contrib.contenttypes.models import ContentType

class Image(models.Model):
    image = models.ImageField(upload_to="images")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

def _generate_filename(instance, filename):
    file_extension = os.path.splitext(filename)[1]
    uuid_filename = f"{uuid.uuid4()}{file_extension}"
    return os.path.join('images/products/', uuid_filename)


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE)
    title = models.CharField(max_length=127)
    description = models.TextField()
    measure = models.CharField(choices=MEASURE_TYPES, max_length=15)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to=_generate_filename, null=True, blank=True)
    barcode = models.CharField(max_length=31)
    barcode_type = models.CharField(max_length=31)

    def __str__(self):
        return self.title

def gen_():
    for i in range(20000):
        print(i)
        id = uuid.uuid4()
        if not Product.objects.filter(id=id).exists():
            Product.objects.create( 
                id=id,
        category_id = 1,
        title= fake.word(),
        description= fake.text(),
        measure= "kg",
        price= fake.random_int(min=10, max=1000),
        barcode= fake.isbn13(),
        barcode_type= "EAN-13"
        )
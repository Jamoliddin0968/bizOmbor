from django.contrib import admin

from .models import Product
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import Image, Product
class ImageInline(GenericTabularInline):
    model = Image
class ProductAdmin(admin.ModelAdmin):
    inlines = [
ImageInline,
]
admin.site.register(Product, ProductAdmin)
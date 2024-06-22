from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import Image, Product


class ImageInline(GenericTabularInline):
    model = Image


class ProductAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    inlines = [
        ImageInline,
    ]


admin.site.register(Product, ProductAdmin)

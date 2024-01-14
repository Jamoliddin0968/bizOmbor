from django_filters import rest_framework as filters

from .models import Product


class ProductFilter(filters.FilterSet):
    store = filters.NumberFilter()
    barcode = filters.CharFilter(min_length=1)
    barcode_type = filters.CharFilter(min_length=1)

    class Meta:
        model = Product
        fields = ['barcode', 'barcode_type', 'store']

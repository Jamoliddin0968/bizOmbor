from django.db import transaction
from rest_framework import serializers

from apps.products.models import Product
from apps.versions.models import Version


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Product


class _ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('version',)


class ProductListCreateSerializer(serializers.Serializer):
    product_list = _ProductCreateSerializer(many=True)

    def create(self, validated_data):
        lst = []
        with transaction.atomic:
            version = Version.objects.create()
            for product_data in validated_data.get('product_list', []):
                product = Product(**product_data, version=version)
                lst.append(product)
            product_list = Product.objects.bulk_create(lst)
        return product_list

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if len(data['product_list']) < 0:

            data['version_id'] = data['product_list']['version_id']

from django.shortcuts import render
from rest_framework import  viewsets
from apps.products.models import Product
from apps.products.serializers import ProductSerializer
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
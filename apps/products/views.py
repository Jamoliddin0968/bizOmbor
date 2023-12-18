from django.shortcuts import render
from rest_framework import  viewsets,filters
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

from apps.products.models import Product
# from .filters import ProductFilter

from apps.products.serializers import ProductSerializer
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductRetrieveAPIView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_object(self):
        barcode = self.request.query_params.get('barcode')
        barcode_type = self.request.query_params.get('barcode_type')

        if barcode:
            return Product.objects.get(barcode=barcode)
        elif barcode_type:
            return Product.objects.get(barcode_type=barcode_type)
        else:
            return None

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance is None:
            return Response({'error': 'Product not found'}, status=404)

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
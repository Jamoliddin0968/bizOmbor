from rest_framework import  viewsets
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from apps.products.models import Product
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter
from apps.products.serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter
    @swagger_auto_schema(tags=['Product'], operation_id='list_items')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Product'], operation_id='retrieve_item')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Product'], operation_id='create_item')
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Product'], operation_id='update_item')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Product'], operation_id='partial_update_item')
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Product'], operation_id='destroy_item')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

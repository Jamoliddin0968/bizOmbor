from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from apps.products.models import Product
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter
from apps.products.serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    queryset = Product.objects.all()
    def get_queryset(self):
        user = self.request.user
        if user.is_manager:
            return  Product.objects.filter(store__manager=user)
        return Product.objects.filter(store=user.store)


    permission_classes = [IsAuthenticated,]


    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter

    @extend_schema(tags=['Product'], description='List items', operation_id='list_items')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(tags=['Product'], description='Retrieve an item', operation_id='retrieve_item')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(tags=['Product'], description='Create an item', operation_id='create_item')
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(tags=['Product'], description='Update an item', operation_id='update_item')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(tags=['Product'], description='Partial update an item', operation_id='partial_update_item')
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(tags=['Product'], description='Delete an item', operation_id='destroy_item')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

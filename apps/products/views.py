from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, extend_schema_view
from apps.products.models import Product
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter
from apps.products.serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated

from ..stores.models import Store


@extend_schema_view(
    list=extend_schema(tags=["Product"]),
    retrieve=extend_schema(tags=["Product"]),
    create=extend_schema(tags=["Product"]),
    update=extend_schema(tags=["Product"]),
    partial_update=extend_schema(tags=["Product"]),
    destroy=extend_schema(tags=["Product"])
)
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, ]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter
    queryset = Product.objects.all()

    def get_queryset(self):
        user = self.request.user
        if user.is_manager:
            return  Product.objects.filter(store__manager=user).all()
        return Product.objects.filter(store=user.store).all()

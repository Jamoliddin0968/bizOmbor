from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.products.models import Product
from apps.products.serializers import ProductSerializer
from .filters import ProductFilter


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


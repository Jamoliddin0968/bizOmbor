from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.categories.models import Category
from apps.categories.serializers import CategorySerializer
from apps.users.permissions import IsManager


@extend_schema_view(
    list=extend_schema(tags=["Category"]),
    retrieve=extend_schema(tags=["Category"]),
    create=extend_schema(tags=["Category"]),
    update=extend_schema(tags=["Category"]),
    partial_update=extend_schema(tags=["Category"]),
    destroy=extend_schema(tags=["Category"])
)
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsManager]

    queryset = Category.objects.all()
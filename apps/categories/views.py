from rest_framework import viewsets
from drf_spectacular.utils import extend_schema
from apps.categories.serializers import CategorySerializer
from apps.categories.models import Category

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    @extend_schema(tags=['Categories'], description='List categories', operation_id='list_categories')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(tags=['Categories'], description='Retrieve a category', operation_id='retrieve_category')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(tags=['Categories'], description='Create a category', operation_id='create_category')
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(tags=['Categories'], description='Update a category', operation_id='update_category')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(tags=['Categories'], description='Partial update a category', operation_id='partial_update_category')
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(tags=['Categories'], description='Delete a category', operation_id='destroy_category')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

from rest_framework import status, viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from .models import Sale
from .serializers import SaleCreateSerializer, SaleSerializer


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    http_method_names = ['post', 'get']

    @extend_schema(
        tags=['Sale'],
        request=SaleCreateSerializer,
        responses={status.HTTP_201_CREATED: SaleSerializer}
    )
    def create(self, request, *args, **kwargs):
        serializer = SaleCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        sale_object = serializer.save()
        serializer = SaleSerializer(sale_object)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @extend_schema(tags=['Sale'])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(tags=['Sale'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

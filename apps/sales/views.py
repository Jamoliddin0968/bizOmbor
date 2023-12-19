from drf_yasg.utils import swagger_auto_schema
from rest_framework import status,viewsets
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.response import Response

from .models import Sale
from .serializers import SaleCreateSerializer,SaleSerializer



class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    http_method_names = ['post','get']

    @swagger_auto_schema(
        request_body=SaleCreateSerializer,
    )
    def create(self, request, *args, **kwargs):
        serializer = SaleCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        sale_object = serializer.save()
        serializer = SaleSerializer(sale_object)
        # headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)






from rest_framework.generics import CreateAPIView
from .models import Sale
from .serializers import SaleCreateSerializer,SaleSerializer


class SaleCreateAPIView(CreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleCreateSerializer

    # @extend_schema(
    #     request=SaleCreateSerializer,
    #     responses={201:SaleSerializer },
    # )
    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)
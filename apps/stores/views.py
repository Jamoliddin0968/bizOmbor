from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.users.permissions import IsManager
from .models import Store
from .serializers import StoreSerializer
from rest_framework.decorators import action

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticated, IsManager]

    def perform_create(self, serializer):
        serializer.save(manager=self.request.user)

    @action(methods=['post',])
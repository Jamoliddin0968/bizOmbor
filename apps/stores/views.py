from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.users.permissions import IsManager
from .models import Store
from .serializers import StoreSerializer


@extend_schema_view(
    list=extend_schema(tags=["Store"]),
    retrieve=extend_schema(tags=["Store"]),
    create=extend_schema(tags=["Store"]),
    update=extend_schema(tags=["Store"]),
    partial_update=extend_schema(tags=["Store"]),
    destroy=extend_schema(tags=["Store"])
)
class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticated, IsManager]

    def get_queryset(self):
        user = self.request.user
        return Store.objects.filter(manager=user)

    def perform_create(self, serializer):
        serializer.save(manager=self.request.user)

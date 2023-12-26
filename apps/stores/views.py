from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.users.permissions import IsManager
from .models import Store,StoreUser
from .serializers import StoreSerializer, StoreUserCreateSerializer

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticated, IsManager]

    def get_queryset(self):
        user = self.request.user
        return Store.objects.filter(manager=user)
    @extend_schema(tags=['Store'])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(tags=['Store'])
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(tags=['Store'])
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(tags=['Store'])
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(tags=['Store'])
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(manager=self.request.user)

class StoreUserViewSet(viewsets.ModelViewSet):
    serializer_class = StoreUserCreateSerializer
    queryset = StoreUser.objects.all()
    permission_classes = [IsManager,IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return StoreUser.objects.filter(store__manager=user)
    @extend_schema(tags=['Store'])
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save()


    @extend_schema(tags=['Store'],)
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
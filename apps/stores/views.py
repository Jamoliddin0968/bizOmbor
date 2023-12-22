from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.users.permissions import IsManager
from .models import Store
from .serializers import StoreSerializer, StoreUserCreateSerializer
from rest_framework.decorators import action

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticated, IsManager]

    @extend_schema(tags=['Store'])
    def create(self, request, *args, **kwargs):
        """
        Creates a new store.
        """
        return super().create(request, *args, **kwargs)

    @extend_schema(tags=['Store'])
    def retrieve(self, request, *args, **kwargs):
        """
        Retrieves a specific store by ID.
        """
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(tags=['Store'])
    def update(self, request, *args, **kwargs):
        """
        Updates a specific store by ID.
        """
        return super().update(request, *args, **kwargs)

    @extend_schema(tags=['Store'])
    def partial_update(self, request, *args, **kwargs):
        """
        Partially updates a specific store by ID.
        """
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(tags=['Store'])
    def destroy(self, request, *args, **kwargs):
        """
        Deletes a specific store by ID.
        """
        return super().destroy(request, *args, **kwargs)

    @extend_schema(tags=['Store'])
    @action(detail=True, methods=['post'])
    def custom_action(self, request, pk=None):
        """
        Perform a custom action on a specific store by ID.
        """
        # Your custom action logic here
        return Response("Custom action performed", status=status.HTTP_200_OK)


    def perform_create(self, serializer):
        serializer.save(manager=self.request.user)

    @extend_schema(tags=['Store'], description='Add new user to store',
                   request=StoreUserCreateSerializer,
                   responses={status.HTTP_201_CREATED:StoreUserCreateSerializer})
    @action(methods=['post',],detail=False)
    def user(self,request,*args,**kwargs):
        serializer = StoreUserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @extend_schema(tags=['Store'], description='Add new user to store',
                   request=StoreUserCreateSerializer,
                   responses={status.HTTP_201_CREATED: StoreUserCreateSerializer})

    @action(methods=['delete', ], detail=False)
    def user(self, request, *args, **kwargs):
        serializer = StoreUserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
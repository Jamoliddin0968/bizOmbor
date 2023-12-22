from drf_spectacular.utils import extend_schema
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.users.permissions import IsManager
from .models import Store
from .serializers import StoreSerializer,StoreUserCreateSerializer
from rest_framework.decorators import action

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticated, IsManager]

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

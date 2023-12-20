from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .permissions import IsSuperUser
from .models import User
from .serializers import ManagerSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ManagerSerializer
    permission_classes = [IsAuthenticated, IsSuperUser]

    @swagger_auto_schema(tags=['Manager'], operation_id='list_users')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Manager'], operation_id='retrieve_user')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Manager'], operation_id='create_user')
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Manager'], operation_id='update_user')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Manager'], operation_id='partial_update_user')
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(tags=['Manager'], operation_id='destroy_user')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSuperUser, IsManager
from .models import Manager, Worker,User
from .serializers import ManagerSerializer, WorkerSerializer,UserSerializer
from drf_spectacular.utils import extend_schema
from rest_framework.generics import RetrieveUpdateAPIView

import jwt
from rest_framework import authentication
from rest_framework import exceptions
from django.conf import settings
from apps.users.models import User
class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    permission_classes = [IsAuthenticated, IsManager]

    @extend_schema(tags=['User'], description='List users')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(tags=['User'], description='Retrieve a user')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def perform_create(self, serializer):
        pass
    @extend_schema(tags=['User'], description='Create a user')
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(tags=['User'], description='Update a user')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(tags=['User'], description='Partial update a user')
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(tags=['User'], description='Delete a user')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    permission_classes = [IsAuthenticated, IsSuperUser]

    @extend_schema(tags=['Manager'], description='List managers')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(tags=['Manager'], description='Retrieve a manager')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(tags=['Manager'], description='Create a manager')
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(tags=['Manager'], description='Update a manager')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(tags=['Manager'], description='Partial update a manager')
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(tags=['Manager'], description='Delete a manager')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class TestApiView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated,]
    def get_object(self):
        return self.request.user

    @extend_schema(tags=['Users'], description='Retrieve')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


    @extend_schema(tags=['Users',], description='Update a manager')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(tags=['Users',], description='Partial update a manager')
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


class CustomJWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')

        if not auth_header or not auth_header.startswith('Bearer '):
            return None

        token = auth_header.split(' ')[1]

        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            user_id = payload['user_id']  # Modify this according to your token payload
            user = User.objects.get(pk=user_id)

            # You can add additional checks/validation here if needed

            return (user, token)

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Token has expired')

        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed('Invalid token')

        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('User not found')
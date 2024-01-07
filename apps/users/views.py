from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import  IsManager
from .models import User
from .serializers import UserSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.generics import RetrieveUpdateAPIView

import jwt
from rest_framework import authentication
from rest_framework import exceptions
from django.conf import settings
from apps.users.models import User


@extend_schema_view(
    retrieve=extend_schema(tags=["Category"]),
    update=extend_schema(tags=["Category"]),
    partial_update=extend_schema(tags=["Category"]),
)
class UserViewSet(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = User
    permission_classes = [IsAuthenticated,]

    def get_object(self):
        return self.request.user




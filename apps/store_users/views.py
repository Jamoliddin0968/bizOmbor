from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.users.models import User
from apps.users.permissions import IsManager
from .models import StoreUser
from .serializers import StoreUserCreateSerializer, PasswordChangeSerializer, StoreUserSerializer


@extend_schema_view(
    list=extend_schema(tags=["Store-User"]),
    retrieve=extend_schema(tags=["Store-User"]),
    create=extend_schema(tags=["Store-User"]),
    update=extend_schema(tags=["Store-User"]),
    partial_update=extend_schema(tags=["Store-User"]),
    destroy=extend_schema(tags=["Store-User"])
)
class StoreUserViewSet(viewsets.ModelViewSet):
    queryset = StoreUser.objects.all()
    serializer_class = StoreUserSerializer
    permission_classes = [IsAuthenticated, IsManager]

    def get_queryset(self):
        return StoreUser.objects.filter(store__manager=self.request.user).all()

    http_method_names = ['get', 'delete']


@extend_schema_view(
    list=extend_schema(tags=["Store-User"]),
    # retrieve=extend_schema(tags=["Store-User"]),
    create=extend_schema(tags=["Store-User"])
)
class StoreUserCreateApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = StoreUserCreateSerializer
    permission_classes = [IsAuthenticated, IsManager]


class PasswordChangeView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = PasswordChangeSerializer

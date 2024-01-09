from drf_spectacular.utils import extend_schema
from rest_framework.response import Response

from .models import StoreUser
from .serializers import StoreUserCreateSerializer, PasswordChangeSerializer, StoreUserSerializer
from rest_framework.permissions import IsAuthenticated
from apps.users.permissions import IsManager
from rest_framework import viewsets, status
from apps.users.models import  User

from rest_framework.generics import UpdateAPIView

class StoreUserViewSet(viewsets.ModelViewSet):
    queryset = StoreUser.objects.all()
    serializer_class = StoreUserSerializer
    permission_classes = [IsAuthenticated,IsManager]

    def get_queryset(self):
        return StoreUser.objects.filter(store__manager=self.request.user).all()

    http_method_names = ['get','post','delete']

    @extend_schema(
        request=StoreUserCreateSerializer,
        responses={204: None,201:StoreUserCreateSerializer}
    )
    def create(self, request, *args, **kwargs):
        serializer = StoreUserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        # serializer = self.serializer_class(da)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class PasswordChangeView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = PasswordChangeSerializer

from .models import StoreUser
from .serializers import StoreUserCreateSerializer,PasswordChangeSerializer
from rest_framework.permissions import IsAuthenticated
from apps.users.permissions import IsManager
from rest_framework import viewsets
from apps.users.models import  User

from rest_framework.generics import UpdateAPIView
class StoreUserViewSet(viewsets.ModelViewSet):
    queryset = StoreUser.objects.all()
    serializer_class = StoreUserCreateSerializer
    permission_classes = [IsAuthenticated,IsManager]

    def get_queryset(self):
        return StoreUser.objects.all(store=self.request.user)

    http_method_names = ['get','post','delete']

class PasswordChangeView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = PasswordChangeSerializer

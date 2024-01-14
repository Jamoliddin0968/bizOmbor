from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.users.models import User
from .serializers import UserSerializer


@extend_schema_view(
    retrieve=extend_schema(tags=["User"]),
    update=extend_schema(tags=["User"]),
    partial_update=extend_schema(tags=["User"]),
)
class UserViewSet(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        return self.request.user

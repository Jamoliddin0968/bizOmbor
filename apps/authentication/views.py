from apps.users.models import User
from apps.users.serializers import UserSerializer
from rest_framework.generics import CreateAPIView
class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
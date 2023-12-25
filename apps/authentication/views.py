import datetime
from django.contrib.auth import authenticate
from django.db.models import Q
import jwt
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from apps.users.models import User
from .serializers import LoginSerializer
from apps.users.models import Seans
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import get_authorization_header, BaseAuthentication
MANAGER_EXPIRE = 2*60
SECRET_KEY = "skladum_dsfghj"
WORKER_EXPIRE = 1

algorithm='HS256'




class LoginBase(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    is_manager = None  # This will be set in LoginManager or LoginWorker
    expire_days=0
    def generate_token(self, user, device_id, user_agent_data):
        current_date = datetime.datetime.now()
        next_day = current_date + datetime.timedelta(days=self.expire_days)
        unix_timestamp = int(next_day.timestamp())

        Seans.objects.filter(user=user).update(is_active=False)
        seans = Seans.objects.create(user=user, device_id=device_id,
                                     user_agent=user_agent_data, expire_date=unix_timestamp)
        payload = {'sub': seans.id}
        jwt_token = jwt.encode(payload, SECRET_KEY,algorithm=algorithm)
        return jwt_token

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        device_id = serializer.validated_data.get('device_id')
        user = authenticate(username=username, password=password)
        if user and user.is_manager == self.is_manager:
            user_agent_data = request.META.get('HTTP_USER_AGENT', '')

            jwt_token = self.generate_token(user, device_id, user_agent_data)
            return Response(data={'access': jwt_token}, status=200)
        else:
            raise AuthenticationFailed("Username or password incorrect")


class LoginManager(LoginBase):
    is_manager = True
    expire_days = 120


class LoginWorker(LoginBase):
    is_manager = False
    expire_days = 1


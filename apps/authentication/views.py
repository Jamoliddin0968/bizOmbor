from datetime import datetime,timedelta

import jwt
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.store_users.models import StoreUser
from apps.users.models import Seans
from apps.users.models import User, UserTarif
from .serializers import LoginSerializer

MANAGER_EXPIRE = 2 * 60
SECRET_KEY = "skladum_dsfghj"
WORKER_EXPIRE = 1

algorithm = 'HS256'


class LoginBase(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    is_manager = None  # This will be set in LoginManager or LoginWorker
    expire_days = 0

    def generate_token(self, user, device_id, user_agent_data):
        current_date = datetime.now()
        next_day = current_date + timedelta(days=self.expire_days)
        unix_timestamp = int(next_day.timestamp())

        Seans.objects.filter(user=user).update(is_active=False)
        seans = Seans.objects.create(user=user, device_id=device_id,
                                     user_agent=user_agent_data, expire_date=unix_timestamp)
        payload = {'sub': seans.id}
        jwt_token = jwt.encode(payload, SECRET_KEY, algorithm=algorithm)
        return jwt_token

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        device_id = serializer.validated_data.get('device_id')
        user = authenticate(username=username, password=password)

        if user and user.is_manager == False:
            current_date = datetime.now().date()
            store = StoreUser.objects.filter(user=user).first()
            if  store:
                manager = store.manager
                tarif = UserTarif.objects.filter(user=manager)
                if not tarif:
                    if current_date > tarif.expire:
                        pass
                    else:
                        raise ValidationError(detail="Please buy tarif")
                else:
                    raise ValidationError(detail="Your store dont have tarif")
            else:
                raise ValidationError(detail="You don't have story")

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

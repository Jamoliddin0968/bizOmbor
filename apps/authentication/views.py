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


class LoginBase(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    is_manager = None  # This will be set in LoginManager or LoginWorker
    expire_days=0
    def generate_token(self, user, device_id, user_agent_data):
        current_date = datetime.datetime.now()
        next_day = current_date + datetime.timedelta(days=self.expire_days)
        unix_timestamp = int(next_day.timestamp())

        Seans.objects.filter(user=user).delete()
        seans = Seans.objects.create(user=user, device_id=device_id,
                                     user_agent=user_agent_data, expire_date=unix_timestamp)
        payload = {'sub': seans.id}
        jwt_token = jwt.encode(payload, SECRET_KEY)
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
class JWTAuthentication(BaseAuthentication):
    model = User
    def get_model(self):
        return User

    def authenticate(self, request):
        auth = get_authorization_header(request).split()
        if not auth or auth[0].lower() != b'bearer':
            return None

        if len(auth) == 1:
            msg = 'Invalid token header. No credentials provided.'
            raise AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = 'Invalid token header'
            raise AuthenticationFailed(msg)

        try:
            token = auth[1]
            if token == "null":
                msg = 'Null token not allowed'
                raise AuthenticationFailed(msg)
        except UnicodeError:
            msg = 'Invalid token header. Token string should not contain invalid characters.'
            raise AuthenticationFailed(msg)

        return self.authenticate_credentials(token)

    def authenticate_credentials(self, token):
        model = self.get_model()
        payload = jwt.decode(token,SECRET_KEY)
        seans_id = payload.get('sub')
        msg = {'Error': "Token mismatch", 'status': "401"}
        try:
            seans = Seans.objects.filter(Q(id = seans_id) & Q(is_active = True)).first()
            current_date = datetime.datetime.now()
            unix_timestamp = int(current_date.timestamp())
            if seans.expire_date < unix_timestamp and seans.user is not None:
                return (seans.user, token)
        except:
            pass
        raise AuthenticationFailed("token is invalid")

    def authenticate_header(self, request):
        return 'BEARER'



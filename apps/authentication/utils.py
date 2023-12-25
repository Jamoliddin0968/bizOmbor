import datetime
from django.contrib.auth import authenticate
from django.db.models import Q
import jwt
from apps.users.models import User
from apps.users.models import Seans
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import get_authorization_header, BaseAuthentication
MANAGER_EXPIRE = 2*60
SECRET_KEY = "skladum_dsfghj"
WORKER_EXPIRE = 1

algorithm="HS256"

class SafeJWTAuthentication(BaseAuthentication):
    model = None
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
        try:
            model = self.get_model()
            payload = jwt.decode(token, SECRET_KEY, algorithms=[algorithm, ])
            seans_id = payload.get('sub')
            msg = {'Error': "Token mismatch", 'status': "401"}
            seans = Seans.objects.filter(Q(id = seans_id) & Q(is_active = True)).first()
            current_date = datetime.datetime.now()
            unix_timestamp = int(current_date.timestamp())

            if seans.expire_date > unix_timestamp and seans.user is not None:
                return (seans.user, token)
        except:
            pass
        raise AuthenticationFailed("token is invalid")

    def authenticate_header(self, request):
        return 'BEARER'


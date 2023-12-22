from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

from django.urls import path
urlpatterns = [
    path('manager/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/', TokenObtainPairView.as_view(), name='token_refresh'),
]
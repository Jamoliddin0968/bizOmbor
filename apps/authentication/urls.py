from django.urls import path, include
from .views import (
    UserCreateAPIView,
)
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path("sign_up/", UserCreateAPIView.as_view()),
]

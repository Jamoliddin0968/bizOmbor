from django.urls import path

from .views import (
    UserViewSet
)

urlpatterns = [
    path("users/me/", UserViewSet.as_view()),
]

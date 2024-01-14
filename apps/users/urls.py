from django.urls import path

from .views import (
    UserViewSet
)

urlpatterns = [
    path("me/", UserViewSet.as_view()),
]

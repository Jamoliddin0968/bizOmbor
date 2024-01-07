from django.urls import path, include
from .views import (
    UserViewSet
)





urlpatterns = [
    path("me/",UserViewSet.as_view()),
]


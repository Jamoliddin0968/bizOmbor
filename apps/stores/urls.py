from django.urls import path, include
from .views import (
    StoreViewSet,
)
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("", StoreViewSet)


urlpatterns = [
    path("", include(router.urls)),
]

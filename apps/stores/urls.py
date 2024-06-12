from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    StoreViewSet,
)

router = DefaultRouter()
router.register("store", StoreViewSet)
# router.register("store-user",StoreUserViewSet)


urlpatterns = [
    path("", include(router.urls)),
]

from django.urls import path, include
from .views import (
    StoreViewSet,
)
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("", StoreViewSet)
# router.register("store-user",StoreUserViewSet)


urlpatterns = [
    path("", include(router.urls)),
]

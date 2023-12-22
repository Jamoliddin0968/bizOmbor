from django.urls import path, include
from .views import (
    StoreViewSet,
    StoreUserViewSet
)
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("stores", StoreViewSet)
router.register("store-user",StoreUserViewSet)


urlpatterns = [
    path("", include(router.urls)),
]

from django.urls import path, include
from .views import (
    WorkerViewSet,ManagerViewSet
)
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("workers/", WorkerViewSet)
router.register('managers/',ManagerViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

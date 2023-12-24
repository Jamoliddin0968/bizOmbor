from django.urls import path, include
from .views import (
    WorkerViewSet,ManagerViewSet,TestApiView
)
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
# router.register("workers", WorkerViewSet)
router.register('managers',ManagerViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('test/',TestApiView.as_view())
]

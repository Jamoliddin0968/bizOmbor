from django.urls import path, include
from .views import (
    ManagerViewSet,TestApiView
)
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
# router.register("workers", WorkerViewSet)
router.register('managers',ManagerViewSet)
# router.register('users',TestApiView)

urlpatterns = [
    path("me/",TestApiView.as_view()),
]
urlpatterns+=router.urls

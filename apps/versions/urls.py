from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import VersionProductListApiView, VersionViewSet

router = DefaultRouter()
router.register('versions', VersionViewSet, basename='version')
urlpatterns = [
    path('versions/<int:version_id>/products',
         VersionProductListApiView.as_view()),
    path('', include(router.urls)),
]

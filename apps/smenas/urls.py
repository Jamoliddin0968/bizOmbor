from django.urls import path, include
from rest_framework import routers

from .views import SmenaViewSet

router = routers.DefaultRouter()
router.register('smenas', SmenaViewSet)
urlpatterns = [
    path('', include(router.urls)),
]

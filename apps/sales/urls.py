from django.urls import path, include
from rest_framework import routers

from .views import SaleViewSet

router = routers.DefaultRouter()
router.register('', SaleViewSet)
urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.products.views import ProductViewSet

router = DefaultRouter()
router.register('', ProductViewSet)
urlpatterns = [
    path('', include(router.urls)),
]

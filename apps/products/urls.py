from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.products.views import ProductListCreateAPIView, ProductViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)
urlpatterns = [
    path('product-list/', ProductListCreateAPIView.as_view()),
    path('', include(router.urls)),
]

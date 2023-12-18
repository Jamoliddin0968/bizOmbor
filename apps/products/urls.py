from django.urls import  path,include
from apps.products.views import ProductViewSet
from rest_framework.routers import DefaultRouter
from .views import ProductRetrieveAPIView
router = DefaultRouter()
router.register('',ProductViewSet)
urlpatterns = [
    path('',include(router.urls)),
    path('barcode/', ProductRetrieveAPIView.as_view(), name='product-retrieve'),
]
from django.urls import  path,include
from .views import SaleViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register('',SaleViewSet)
urlpatterns = [
    path('',include(router.urls)),
]
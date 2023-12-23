from django.urls import  path,include
from .views import CashBoxViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('',CashBoxViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
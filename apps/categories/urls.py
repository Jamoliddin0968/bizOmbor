from django.urls import  path,include
from apps.categories.views import CategoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('',CategoryViewSet,basename='category')

urlpatterns = [
    path('',include(router.urls)),
]
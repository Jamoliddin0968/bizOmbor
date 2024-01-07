from django.urls import path, include
from .views import StoreUserViewSet,PasswordChangeView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('',StoreUserViewSet,basename='Store user')

urlpatterns = [
    path('',include(router.urls)),
    path('<int:pk>/',PasswordChangeView.as_view())
]
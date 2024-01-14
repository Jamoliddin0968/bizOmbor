from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import StoreUserViewSet, PasswordChangeView, StoreUserCreateApiView

router = DefaultRouter()
router.register('', StoreUserViewSet, basename='Store user')

urlpatterns = [
    path('new/', StoreUserCreateApiView.as_view()),
    path('', include(router.urls)),

    path('<int:pk>/', PasswordChangeView.as_view())
]

from django.urls import path
from .views import StoreUserCreateAPIView

urlpatterns = [
    path('', StoreUserCreateAPIView.as_view(), name='storeuser-create'),
    # path('storeusers/delete/<int:pk>/', StoreUserDeleteAPIView.as_view(), name='storeuser-delete'),
]

from django.urls import  path,include
from .views import SaleCreateAPIView

urlpatterns = [
    path('', SaleCreateAPIView.as_view(), name='sale-create'),
]
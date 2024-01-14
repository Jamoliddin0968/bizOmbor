from django.urls import  path,include
from .views import RecoveryCreateApiView

urlpatterns = [
    path('',RecoveryCreateApiView.as_view()),
]
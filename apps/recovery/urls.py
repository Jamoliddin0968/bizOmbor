from django.urls import path

from .views import RecoveryCreateApiView

urlpatterns = [
    path('', RecoveryCreateApiView.as_view()),
]

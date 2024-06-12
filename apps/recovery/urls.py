from django.urls import path

from .views import RecoveryCreateApiView

urlpatterns = [
    path('recovery/', RecoveryCreateApiView.as_view()),
]

from .views import LoginManager,LoginWorker
from django.urls import path
urlpatterns = [
    path('manager/', LoginManager.as_view(), name='login+for_manager'),
    path('worker/',LoginWorker.as_view(),name="login_for_worker")
]
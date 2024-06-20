"""
    asosiy manager_urls.py
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .swagger_urls import swagger_urlpatterns

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

token_urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login/',include('apps.authentication.urls')),
    path('api/v1/',include('apps.products.urls')),
    path('api/v1/',include('apps.categories.urls')),
    # path('api/v1/',include('apps.sales.urls')),
    path("api/v1/", include("apps.users.urls")),
    # path("api/v1/",include('apps.stores.urls')),
    # path("api/v1/",include('apps.store_users.urls')),
    # path("api/v1/",include('apps.recovery.urls')),
    # path("api/v1/",include('apps.sync.urls')),
    # path("api/v1/",include('apps.smenas.urls'))
]

urlpatterns+=swagger_urlpatterns
urlpatterns+=token_urlpatterns
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
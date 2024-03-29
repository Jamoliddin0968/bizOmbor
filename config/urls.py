"""
    asosiy manager_urls.py
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .swagger_urls import swagger_urlpatterns




urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',include('apps.authentication.urls')),
    path('api/v1/products/',include('apps.products.urls')),
    path('api/v1/categories/',include('apps.categories.urls')),
    path('api/v1/sales/',include('apps.sales.urls')),
    path("api/v1/users/", include("apps.users.urls")),
    path("api/v1/store/",include('apps.stores.urls')),
    path("api/v1/store-user/",include('apps.store_users.urls')),
    path("api/v1/recovery/",include('apps.recovery.urls')),
    path("api/v1/sync/",include('apps.sync.urls')),
    path("api/v1/sync/",include('apps.smenas.urls'))
]

urlpatterns+=swagger_urlpatterns
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
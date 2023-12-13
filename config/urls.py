"""
    asosiy urls.py
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .yasg_urls import drf_yasg_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/products/',include('apps.products.urls')),
    path('api/v1/categories/',include('apps.categories.urls')),
]
urlpatterns+=drf_yasg_urlpatterns

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
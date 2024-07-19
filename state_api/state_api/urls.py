from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('swagger', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/states/', include('api.urls')),
    path('admin/', admin.site.urls),
]
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("apps.portfolio.urls")),
    path('api/', include("apps.portfolio_api.urls")),
    path('dashboard/', include("apps.dashboard.urls")),
    path('api-auth/', include('rest_framework.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "apps.portfolio.views.error_404"
handler500 = "apps.portfolio.views.error_500"
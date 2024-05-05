from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('public.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('api/', include([
        path('auth/', include('rest_framework.urls')),
        path('users/', include('users.urls')),
        path('tickets/', include('tickets.urls')),
        path('workspace/', include('workspace.urls')),
    ])),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

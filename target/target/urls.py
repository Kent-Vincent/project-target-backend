from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('public.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('api/', include([
        path('auth/', include('rest_framework.urls')),
        path('users/', include('users.urls')),
    ])),
]

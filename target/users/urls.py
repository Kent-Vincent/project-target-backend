from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import LoginView, AuthView

urlpatterns = [
    path('login/', LoginView.as_view({
        'post': 'login',
    })),
    path('auth/', AuthView.as_view({
        'get': 'auth',
    })),
]

urlpatterns = format_suffix_patterns(urlpatterns)
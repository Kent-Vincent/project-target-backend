from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import LoginView, AuthView, RegisterUserView, CurrentUserView

urlpatterns = [
    path('login/', LoginView.as_view({
        'post': 'login',
    })),
    path('register/', RegisterUserView.as_view()),
    path('auth/', AuthView.as_view({
        'get': 'auth',
    })),
    path('currentUser/', CurrentUserView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
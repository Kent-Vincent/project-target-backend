from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from accounts import views

urlpatterns = [
    path('profile/', views.Accounts.as_view()),
    path('api/auth/', views.CustomAuthToken.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
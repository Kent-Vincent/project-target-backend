from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from users import views

urlpatterns = [
    path('profile/', views.Users.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
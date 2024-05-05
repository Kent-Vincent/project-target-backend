from django.urls import path
from .views import current_workspace

urlpatterns = [
    path('current/', current_workspace, name='current_workspace'),
]

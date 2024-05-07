from django.urls import path
from .views import current_workspace, current_stage, create_workspace

urlpatterns = [
    path('current/workspace/', current_workspace, name='current_workspace'),
    path('current/stage/', current_stage, name='current_stage'),
    path('create/workspace/', create_workspace, name='create_workspace'),
]

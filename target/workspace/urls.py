from django.urls import path
from .views import current_workspace, current_stage

urlpatterns = [
    path('current/workspace', current_workspace, name='current_workspace'),
    path('current/stage', current_stage, name='current_stage')
]

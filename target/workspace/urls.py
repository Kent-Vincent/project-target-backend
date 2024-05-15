from django.urls import path
from .views import current_workspace, create_workspace, get_workspace_by_id, get_stages_by_workspace, create_stage

urlpatterns = [
    path('current/workspace/', current_workspace, name='current_workspace'),
    # path('current/stage/', current_stage, name='current_stage'),
    path('create/workspace/', create_workspace, name='create_workspace'),
    path('<int:workspace_ID>', get_workspace_by_id, name='get_workspace_by_id'),
    path('stages/<int:workspace_id>', get_stages_by_workspace, name='get_stages_by_workspace'),
    path('create/stage/<int:workspace_ID>', create_stage, name='create_stage'),
]

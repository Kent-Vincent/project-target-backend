from django.shortcuts import render
from .models import Workspace

class WorkspaceDisplay():
    queryset = Workspace.objects.all()

    

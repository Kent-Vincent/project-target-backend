from django.shortcuts import render
from .models import Workspace

class WorkspaceDisplay():
    tickets = Workspace.objects.filter(ticket)
    # queryset = Workspace.objects.all()

    

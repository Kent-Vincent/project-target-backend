from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Workspace, Stage
from workspace.serializers import WorkspaceSerializer, StageSerializer

@api_view(['GET'])
def current_workspace(request):
    if request.user.is_authenticated:
        try:
            workspace = Workspace.objects.filter(users=request.user).first()
            if workspace:
                serializer = WorkspaceSerializer(workspace)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Workspace not found for this user'}, status=status.HTTP_404_NOT_FOUND)
        except Workspace.DoesNotExist:
            return Response({'error': 'Workspace does not exist'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['GET'])
def current_stage(request):
    if request.user.is_authenticated:
        try:
            workspace = Workspace.objects.filter(users=request.user).first()
            if workspace:
                # Filter the stage based on the workspace
                stage = Stage.objects.filter(workspace=workspace).all()
                if stage:
                    serializer = StageSerializer(stage, many=True)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Stage not found for this workspace'}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'error': 'Workspace not found for this user'}, status=status.HTTP_404_NOT_FOUND)
        except Stage.DoesNotExist:
            return Response({'error': 'Stage does not exist'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

    

  

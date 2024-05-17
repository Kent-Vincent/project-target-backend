from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Workspace, Stage
from workspace.serializers import WorkspaceSerializer, StageSerializer

@api_view(['GET'])
def current_workspace(request):
    if request.user.is_authenticated:
        try:
            workspace = Workspace.objects.filter(users=request.user)
            if workspace:
                serializer = WorkspaceSerializer(workspace, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Workspace not found for this user'}, status=status.HTTP_404_NOT_FOUND)
        except Workspace.DoesNotExist:
            return Response({'error': 'Workspace does not exist'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['GET'])
def get_workspace_by_id(request, workspace_ID):
    if request.user.is_authenticated:
        try:
            workspace = Workspace.objects.filter(users=request.user, workspace_ID=workspace_ID).first()
            if workspace:
                serializer = WorkspaceSerializer(workspace)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Workspace not found for this user'}, status=status.HTTP_404_NOT_FOUND)
        except Workspace.DoesNotExist:
            return Response({'error': 'Workspace does not exist'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['POST'])
def create_workspace(request):
    if request.user.is_authenticated:
        serializer = WorkspaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['users'] = [request.user.users_ID]
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['GET'])
def get_stages_by_workspace(request, workspace_id):
    if request.user.is_authenticated:
        try:
            workspace = Workspace.objects.filter(users=request.user, workspace_ID=workspace_id).first()
            if workspace:
                stages = Stage.objects.filter(workspace=workspace).prefetch_related('tickets').all()
                serializer = StageSerializer(stages, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Workspace not found for this user'}, status=status.HTTP_404_NOT_FOUND)
        except Stage.DoesNotExist:
            return Response({'error': 'Stages do not exist for this workspace'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def create_stage(request, workspace_ID):
    if request.user.is_authenticated:
        try:
            # Assuming you have a Workspace model with a workspace_ID field
            workspace = Workspace.objects.get(users=request.user, workspace_ID=workspace_ID)
            # Assuming you have a Stage model with appropriate fields
            stage_data = {
                'workspace': workspace.id,  # Assuming the workspace field is a ForeignKey
                # Add other fields here based on your Stage model
            }
            serializer = StageSerializer(data=stage_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Workspace.DoesNotExist:
            return Response({'error': 'Workspace not found for this user'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
    

  

from rest_framework import serializers
from .models import Workspace, Stage


class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = '__all__'

class StageSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Stage
        fields = '__all__'

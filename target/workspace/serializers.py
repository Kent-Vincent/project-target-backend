from rest_framework import serializers
from .models import Workspace, Stage
from tickets.serializers import TicketSerializer


class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = '__all__'

class StageSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True, read_only=True)
    class Meta: 
        model = Stage
        fields = '__all__'

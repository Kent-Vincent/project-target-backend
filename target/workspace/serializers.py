from rest_framework import serializers
from .models import Workspace, Stage
from rest_framework import serializers


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = '__all__'

class StageSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Stage
        fields = '__all__'

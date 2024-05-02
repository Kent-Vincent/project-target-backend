from rest_framework import serializers
from .models import Workspace

from rest_framework import serializers

class BoardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = '__all__'

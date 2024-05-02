from rest_framework import serializers
from .models import Workspace

from rest_framework import serializers


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = '__all__'

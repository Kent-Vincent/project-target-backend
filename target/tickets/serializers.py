from rest_framework import serializers
from .models import Tickets

# myapp/serializers.py
from rest_framework import serializers


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = '__all__'

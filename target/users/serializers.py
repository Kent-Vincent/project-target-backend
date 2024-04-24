from rest_framework.serializers import ModelSerializer
from .models import User


class UserSerializer(ModelSerializer):

    class Meta:
        model =  User
        fields = (
            'email',
            'password',
            'first_name',
            'last_name',
        )
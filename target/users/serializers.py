from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) 

    class Meta:
        model =  User
        fields = (
            'users_ID'
            'email',
            'password',
            'first_name',
            'last_name',
            'avatar',
        )

    def create(self, validated_data):
        # Extract password from validated data and hash it before saving
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user
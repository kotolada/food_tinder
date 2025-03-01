from django.contrib.auth.models import User
from rest_framework import serializers
from typing import Any, Dict

class CreateUserSerializer(serializers.ModelSerializer[User]):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data: Dict[str, Any]) -> User:
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        return user


from api.serializers.CreateUserSerializer import CreateUserSerializer
from django.contrib.auth.models import User
from typing import cast


class AuthService:
    @staticmethod
    def create_by_creds(data: CreateUserSerializer) -> User:
        data.is_valid(raise_exception=True)
        data.save()
        return cast(User, data.instance)
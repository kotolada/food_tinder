from api.serializers import CreateUserSerializer


class AuthService:
    def create_by_creds(data: CreateUserSerializer):
        data.is_valid(raise_exception=True)
        data.save()
        return data
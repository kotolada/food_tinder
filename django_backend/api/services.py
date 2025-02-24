from api.serializers import CreateUser


class AuthService:
    def create_by_creds(data: CreateUser):
        data.is_valid(raise_exception=True)
        data.save()
        return data
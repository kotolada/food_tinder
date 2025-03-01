from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from tutorial.quickstart.serializers import UserSerializer
from django.db.models.query import QuerySet

class UserViewSet(viewsets.ModelViewSet[UserSerializer]):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset: QuerySet[User] = User.objects.all().order_by('-date_joined')
    serializer_class: type[UserSerializer] = UserSerializer
    permission_classes: list[type[permissions.BasePermission]] = [permissions.IsAuthenticated]
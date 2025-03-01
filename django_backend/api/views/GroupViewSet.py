from django.contrib.auth.models import Group
from rest_framework import permissions, viewsets
from tutorial.quickstart.serializers import GroupSerializer
from django.db.models.query import QuerySet

class GroupViewSet(viewsets.ModelViewSet[GroupSerializer]):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset: QuerySet[Group] = Group.objects.all().order_by('name')
    serializer_class: type[GroupSerializer] = GroupSerializer
    permission_classes: list[type[permissions.BasePermission]] = [permissions.IsAuthenticated]
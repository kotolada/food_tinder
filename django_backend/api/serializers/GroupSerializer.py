from django.contrib.auth.models import Group
from rest_framework import serializers

class GroupSerializer(serializers.HyperlinkedModelSerializer[Group]):
    class Meta:
        model = Group
        fields = ['url', 'name']
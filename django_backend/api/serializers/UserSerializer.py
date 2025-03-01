from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer[User]):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
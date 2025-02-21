from django.contrib.auth.models import Group, User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


# Recipe and Ingredient Serializers that work with respective models
# (models haven't been defined yet, imagine they're there)

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = [] # Model fields go there
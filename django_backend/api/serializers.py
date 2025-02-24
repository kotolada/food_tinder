from django.contrib.auth.models import Group, User
from rest_framework import serializers
from api.models import Recipe

class CreateUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        return user


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


# Recipe Serializer that works with the respective model

class RecipeSerializer(serializers.ModelSerializer):
    
    name = serializers.CharField(min_length=1, max_length=100, allow_blank=False)
    description = serializers.CharField(max_length=1000, allow_blank=True)
    ingredients = serializers.ListField(allow_empty=False, min_length=1, max_length=50)
    
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'ingredients']
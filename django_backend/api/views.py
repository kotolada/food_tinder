from django.shortcuts import render
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from tutorial.quickstart.serializers import GroupSerializer, UserSerializer
from api.models import Recipe
from api import serializers
from api.serializers import RecipeSerializer
from rest_framework.exceptions import ValidationError


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def list(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)


    def retrieve(self, request, pk):
        recipes = Recipe.objects.get(id=pk)
        serializer = RecipeSerializer(recipes, many=False)
        return Response(serializer.data)



    def update(self, request, pk):
        recipe = Recipe.objects.get(id=pk)
        serializer = RecipeSerializer(instance=recipe, data=request.data)
    
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


    def destroy(self, request, pk):
        recipe = Recipe.objects.get(id=pk)
        recipe.delete()
        return Response('Recipe successfully deleted')



    def create(self, request):
        serializer = RecipeSerializer(data=request.data)

        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
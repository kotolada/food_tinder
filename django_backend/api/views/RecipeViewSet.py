from django.shortcuts import render
from rest_framework import viewsets, status
from api.models.Recipe import Recipe
from api.serializers.RecipeSerializer import RecipeSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.request import Request
from django.db.models.query import QuerySet



class RecipeViewSet(viewsets.ModelViewSet[Recipe]):
    queryset: QuerySet[Recipe] = Recipe.objects.all()
    serializer_class: type[RecipeSerializer] = RecipeSerializer

    def list(self, request: Request) -> Response:
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)


    def retrieve(self, request: Request, pk: int) -> Response:
        recipes = Recipe.objects.get(id=pk)
        serializer = RecipeSerializer(recipes, many=False)
        return Response(serializer.data)


    def update(self, request: Request, pk: int) -> Response:
        recipe = Recipe.objects.get(id=pk)
        serializer = RecipeSerializer(instance=recipe, data=request.data)
    
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
                
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


    def destroy(self, request: Request, pk: int) -> Response:
        recipe = Recipe.objects.get(id=pk)
        recipe.delete()
        return Response('Recipe successfully deleted')


    def create(self, request: Request) -> Response:
        serializer = RecipeSerializer(data=request.data)

        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
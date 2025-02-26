from django.shortcuts import render
from rest_framework import viewsets, status
from api.models.Recipe import Recipe
from api.serializers.RecipeSerializer import RecipeSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response



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
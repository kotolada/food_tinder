from rest_framework import serializers
from api.models.Recipe import Recipe

class RecipeSerializer(serializers.ModelSerializer[Recipe]):
    
    name = serializers.CharField(min_length=1, max_length=100, allow_blank=False)
    description = serializers.CharField(max_length=1000, allow_blank=True)
    ingredients = serializers.ListField(allow_empty=False, min_length=1, max_length=50) # Change the type once we decided what we would put here
    
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'ingredients']
from django.db import models
from typing import cast


class Recipe(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=1000, blank=True, null=True)
    ingredients = models.JSONField(max_length=1000, blank=False, null=False) # Change the type later once we defined what we would store here


    def __str__(self) -> str:
        return cast(str, self.name)
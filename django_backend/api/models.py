from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=1000, blank=True, null=True)
    ingredients = models.CharField(max_length=1000, blank=False, null=False)


    def __str__(self):
        return self.name
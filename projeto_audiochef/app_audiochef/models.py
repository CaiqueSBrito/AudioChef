from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    diets = models.JSONField(default=list)
    dishTypes = models.JSONField(default=list)
    extendedIngredients = models.JSONField(default=list)
    image = models.URLField(blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    vegan = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)
    servings = models.IntegerField(blank=True, null=True)
    readyInMinutes = models.IntegerField(default=0)
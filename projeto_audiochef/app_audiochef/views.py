import requests
import os
from rest_framework.response import Response
from rest_framework import status
from dotenv import load_dotenv
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import *
from . import serializers
load_dotenv()

# Create your views here.
def home (request):
    return render(request, 'app_audiochef/index.html')

class RecipesAPIView(APIView):
    def get(self, request):
        BASE_URL = "https://api.spoonacular.com/recipes/random"

        params = {
            "apiKey": os.getenv("API_KEY"),
            "number": 1
        }

        response = requests.get(BASE_URL, params=params)
        data = response.json()

        recipes = data["recipes"][0]

        result = {
            "diets": recipes["diets"],
            "dishTypes": recipes["dishTypes"],
            "extendedIngredients": recipes["extendedIngredients"],
            "image": recipes["image"],
            "instructions": recipes["instructions"],
            "summary": recipes["summary"],
            "vegan": recipes["vegan"],
            "vegetarian": recipes["vegetarian"],
            "servings": recipes["servings"],
            "readyInMinutes": recipes["readyInMinutes"],
        }

        return Response(result, status=status.HTTP_200_OK)
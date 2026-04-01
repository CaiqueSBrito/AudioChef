import os
import requests
from dotenv import load_dotenv
from .recipe_detail_client import RecipeDetailClient

class SpoonacularDetailClient(RecipeDetailClient):
    def get(self, recipe_id):
        response = requests.get(
            f"https://api.spoonacular.com/recipes/{recipe_id}/information",
            params={"apiKey": os.getenv("API_KEY"), "includeNutrition": "true"}
        )
        return response.json()
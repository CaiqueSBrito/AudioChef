import os
import requests
from dotenv import load_dotenv
from .recipe_random_client import RecipeRandomClient

load_dotenv()

class SpoonacularRandomClient(RecipeRandomClient):
    def get(self):
        response = requests.get(
            "https://api.spoonacular.com/recipes/random",
            params={"apiKey": os.getenv("API_KEY"), "number": 1}
        )
        data = response.json()
        return data.get("recipes", [{}])[0]
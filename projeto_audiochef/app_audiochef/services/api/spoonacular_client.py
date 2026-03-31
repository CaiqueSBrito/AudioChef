import os
import requests
from dotenv import load_dotenv
from .recipe_client import RecipeClient

load_dotenv()

class SpoonacularClient(RecipeClient):
    def get(self):
        response = requests.get(
            "https://api.spoonacular.com/recipes/random",
            params={"apiKey": os.getenv("API_KEY"), "number": 1}
        )
        data = response.json()
        return data.get("recipes", [{}])[0]
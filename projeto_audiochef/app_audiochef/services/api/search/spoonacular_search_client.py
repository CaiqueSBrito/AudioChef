import os
import requests
from .recipe_search_client import RecipeSearchClient

class SpoonacularSearchClient(RecipeSearchClient):
    def search(self, query):
        response = requests.get(
            "https://api.spoonacular.com/recipes/autocomplete",
            params={"apiKey": os.getenv("API_KEY"), "number": 10, "query": query}
        )
        
        # O .json() do endpoint "autocomplete" retorna uma LISTA diretamente,
        data = response.json()
        
        # Como data já é uma lista, podemos retorná-la direto. Se falhar, retorna lista vazia.
        if isinstance(data, list):
            return data
        return []

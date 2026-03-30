from .spoonacular_client import SpoonacularClient


def make_recipe(client=None):
    if client is None:
        client = SpoonacularClient()
    recipe = client.get()
    
    result = {
        "diets": recipe.get("diets"),
        "dishTypes": recipe.get("dishTypes"),
        "extendedIngredients": recipe.get("extendedIngredients"),
        "image": recipe.get("image"),
        "instructions": recipe.get("instructions"),
        "summary": recipe.get("summary"),
        "vegan": recipe.get("vegan"),
        "vegetarian": recipe.get("vegetarian"),
        "servings": recipe.get("servings"),
        "readyInMinutes": recipe.get("readyInMinutes"),
    }

    return result
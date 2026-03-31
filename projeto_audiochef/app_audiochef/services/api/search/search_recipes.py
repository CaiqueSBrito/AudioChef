from .recipe_search_client import RecipeSearchClient


def make_list(client: RecipeSearchClient, query: str):
    recipes = client.search(query)
    
    result = []
    for recipe in recipes:
        recipe_id = recipe.get("id")
        image_url = recipe.get("image")
        
        # O endpoint "autocomplete" retorna apenas "imageType", então montamos a URL manualmente
        if not image_url and recipe_id:
            image_type = recipe.get("imageType", "jpg")
            image_url = f"https://img.spoonacular.com/recipes/{recipe_id}-312x231.{image_type}"
            
        result.append({
            "id": recipe_id,
            "title": recipe.get("title"),
            "image": image_url,
        })
    
    return result
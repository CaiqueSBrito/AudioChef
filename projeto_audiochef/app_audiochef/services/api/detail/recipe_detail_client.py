from abc import ABC, abstractmethod

class RecipeDetailClient(ABC):
    @abstractmethod
    def get(self, recipe_id):
        pass
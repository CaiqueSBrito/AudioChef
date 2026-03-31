from abc import ABC, abstractmethod

class RecipeSearchClient(ABC):
    @abstractmethod
    def search(self, query):
        pass
from abc import ABC, abstractmethod

class RecipeRandomClient(ABC):
    @abstractmethod
    def get(self):
        pass
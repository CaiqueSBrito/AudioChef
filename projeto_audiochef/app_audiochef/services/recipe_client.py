from abc import ABC, abstractmethod


class RecipeClient(ABC):
    @abstractmethod
    def get(self):
        pass
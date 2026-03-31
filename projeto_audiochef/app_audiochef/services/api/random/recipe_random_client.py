from abc import ABC, abstractmethod

#ISSO É UMA INTERFACE!!! 

class RecipeRandomClient(ABC):
    @abstractmethod
    def get(self):
        pass
from abc import ABC, abstractmethod
from typing import List

from project.food import Food


class Animal(ABC):
    FOOD_PREFERENCE: List[str] = []
    WEIGHT_GAIN_RATION: float = 0.0

    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @staticmethod
    @abstractmethod
    def make_sound():
        pass

    def feed(self, food: Food):
        if food.__class__.__name__ not in self.FOOD_PREFERENCE:
            return f"{type(self).__name__} does not eat {type(food).__name__}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity * self.WEIGHT_GAIN_RATION


class Bird(Animal, ABC):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{type(self).__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{type(self).__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"

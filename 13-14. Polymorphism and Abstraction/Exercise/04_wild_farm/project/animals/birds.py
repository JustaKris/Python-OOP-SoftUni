from project.animals.animal import Bird
from project.food import Meat


class Owl(Bird):
    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if isinstance(food, Meat):
            self.food_eaten += food.quantity
            self.weight += 0.25 * food.quantity
        else:
            return f"Owl does not eat {type(food).__name__}!"


class Hen(Bird):
    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        self.food_eaten += food.quantity
        self.weight += 0.35 * food.quantity

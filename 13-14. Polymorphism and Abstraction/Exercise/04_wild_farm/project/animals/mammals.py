from project.animals.animal import Mammal
from project.food import Meat, Vegetable, Fruit


class Mouse(Mammal):
    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if isinstance(food, Fruit) or isinstance(food, Vegetable):
            self.food_eaten += food.quantity
            self.weight += 0.10 * food.quantity
        else:
            return f"Mouse does not eat {type(food).__name__}!"


class Dog(Mammal):
    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if isinstance(food, Meat):
            self.food_eaten += food.quantity
            self.weight += 0.40 * food.quantity
        else:
            return f"Dog does not eat {type(food).__name__}!"


class Cat(Mammal):
    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if isinstance(food, Meat) or isinstance(food, Vegetable):
            self.food_eaten += food.quantity
            self.weight += 0.30 * food.quantity
        else:
            return f"Cat does not eat {type(food).__name__}!"


class Tiger(Mammal):
    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if isinstance(food, Meat):
            self.food_eaten += food.quantity
            self.weight += 1.00 * food.quantity
        else:
            return f"Tiger does not eat {type(food).__name__}!"

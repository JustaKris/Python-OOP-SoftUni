from project.animals.animal import Mammal


class Mouse(Mammal):
    FOOD_PREFERENCE = ["Fruit", "Vegetable"]
    WEIGHT_GAIN_RATION = 0.10

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    FOOD_PREFERENCE = ["Meat"]
    WEIGHT_GAIN_RATION = 0.40

    @staticmethod
    def make_sound():
        return "Woof!"


class Cat(Mammal):
    FOOD_PREFERENCE = ["Meat", "Vegetable"]
    WEIGHT_GAIN_RATION = 0.30

    @staticmethod
    def make_sound():
        return "Meow"


class Tiger(Mammal):
    FOOD_PREFERENCE = ["Meat"]
    WEIGHT_GAIN_RATION = 1.00

    @staticmethod
    def make_sound():
        return "ROAR!!!"

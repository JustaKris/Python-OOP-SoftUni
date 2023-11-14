from project.animals.animal import Mammal


class Mouse(Mammal):
    FOOD_PREFERENCE = ["Fruit", "Vegetable"]
    WEIGHT_GAIN_RATION = 0.10

    @staticmethod
    def make_sound() -> str:
        return "Squeak"


class Dog(Mammal):
    FOOD_PREFERENCE = ["Meat"]
    WEIGHT_GAIN_RATION = 0.40

    @staticmethod
    def make_sound() -> str:
        return "Woof!"


class Cat(Mammal):
    FOOD_PREFERENCE = ["Meat", "Vegetable"]
    WEIGHT_GAIN_RATION = 0.30

    @staticmethod
    def make_sound() -> str:
        return "Meow"


class Tiger(Mammal):
    FOOD_PREFERENCE = ["Meat"]
    WEIGHT_GAIN_RATION = 1.00

    @staticmethod
    def make_sound() -> str:
        return "ROAR!!!"

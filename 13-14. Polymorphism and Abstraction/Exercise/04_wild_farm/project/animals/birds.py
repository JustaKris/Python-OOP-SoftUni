from project.animals.animal import Bird


class Owl(Bird):
    FOOD_PREFERENCE = ["Meat"]
    WEIGHT_GAIN_RATION = 0.25

    @staticmethod
    def make_sound():
        return "Hoot Hoot"


class Hen(Bird):
    FOOD_PREFERENCE = ["Fruit", "Meat", "Seed", "Vegetable"]
    WEIGHT_GAIN_RATION = 0.35

    @staticmethod
    def make_sound():
        return "Cluck"

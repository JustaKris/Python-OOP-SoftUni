class Topping:
    def __init__(self, topping_type: str, weight: float):
        self.topping_type = topping_type
        self.weight = weight

    @property
    def topping_type(self):
        return self.__topping_type

    @topping_type.setter
    def topping_type(self, value: str):
        if value == '':
            raise ValueError("The topping type cannot be an empty string")
        else:
            self.__topping_type = value

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value: float):
        if value > 0:
            self.__weight = value
        else:
            raise ValueError("The weight cannot be less or equal to zero")

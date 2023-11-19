from abc import ABC, abstractmethod
from typing import List


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Triangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return (self.width * self.height) / 2


class AreaCalculator:

    def __init__(self, shapes):
        self.__shapes: List[Shape] = shapes

    @property
    def shapes(self):
        return self.__shapes

    @shapes.setter
    def shapes(self, value):
        if not isinstance(value, list):
            raise AssertionError("'shapes' should be of type 'list'.")
        self.__shapes = value

    @property
    def total_area(self):
        return sum(shape.calculate_area() for shape in self.shapes)

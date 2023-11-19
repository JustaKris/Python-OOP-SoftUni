from abc import ABC, abstractmethod


class Animal(ABC):
    @staticmethod
    @abstractmethod
    def make_sound() -> str:
        pass

    @property
    def species(self) -> str:
        return self.__class__.__name__


class Cat(Animal):
    @staticmethod
    def make_sound() -> str:
        return "meow"


class Chicken(Animal):
    @staticmethod
    def make_sound() -> str:
        return "chirp-chirp"


class Dog(Animal):
    @staticmethod
    def make_sound() -> str:
        return "woof-woof"


class Turtle(Animal):
    @staticmethod
    def make_sound() -> str:
        return "turtle hissing"

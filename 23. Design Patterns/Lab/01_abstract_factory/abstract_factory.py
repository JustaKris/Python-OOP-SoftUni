from abc import ABC, abstractmethod


class AbstractFactory(ABC):

    @abstractmethod
    def create_chair(self):
        raise NotImplementedError()

    @abstractmethod
    def create_sofa(self):
        raise NotImplementedError()

    @abstractmethod
    def create_table(self):
        raise NotImplementedError()


# Item classes
class Chair:

    def __init__(self, name: str):
        self._name = name

    def __str__(self):
        return self._name


class Sofa:

    def __init__(self, name: str):
        self._name = name

    def __str__(self):
        return self._name


class Table:

    def __init__(self, name: str):
        self._name = name

    def __str__(self):
        return self._name


# Factories
class VictorianFactory(AbstractFactory):

    def create_chair(self):
        return Chair('victorian chair')

    def create_sofa(self):
        return Chair('victorian sofa')

    def create_table(self):
        return Chair('victorian table')


class ModernFactory(AbstractFactory):

    def create_chair(self):
        return Chair('modern chair')

    def create_sofa(self):
        return Chair('modern sofa')

    def create_table(self):
        return Chair('modern table')


class FuturisticFactory(AbstractFactory):
    
    def create_chair(self):
        return Chair('futuristic chair')

    def create_sofa(self):
        return Chair('futuristic sofa')

    def create_table(self):
        return Chair('futuristic table')

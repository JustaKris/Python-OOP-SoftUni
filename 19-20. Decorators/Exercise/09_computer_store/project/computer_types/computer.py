from abc import ABC, abstractmethod
from math import log


class Computer(ABC):

    def __init__(self, manufacturer: str, model: str):
        self.__manufacturer = manufacturer
        self.__model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if value.strip() == '':
            raise ValueError("Manufacturer name cannot be empty.")
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value.strip() == '':
            raise ValueError("Model name cannot be empty.")
        self.__model = value

    @property
    @abstractmethod
    def processor_options(self):
        pass

    @property
    @abstractmethod
    def ram_options(self):
        pass

    @property
    @abstractmethod
    def type_str(self):
        pass

    # @property
    # @abstractmethod
    # def max_ram(self):
    #     pass
    #
    # @property
    # def valid_ram(self):
    #     return [2 ** i for i in range(1, int(log(self.max_ram)) + 1)]

    # @abstractmethod
    def configure_computer(self, processor: str, ram: int):
        if processor not in self.processor_options:
            raise ValueError(f"{processor} is not compatible with {self.type_str} {self.manufacturer} {self.model}!")
        if ram not in self.ram_options:
            raise ValueError(f"{ram}GB RAM is not compatible with {self.type_str} {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        self.price = self.ram_options[ram] + self.processor_options[processor]

        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price}$."

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"

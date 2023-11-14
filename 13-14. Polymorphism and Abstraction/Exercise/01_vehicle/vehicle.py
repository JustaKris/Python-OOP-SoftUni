from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: int):
        pass

    @abstractmethod
    def refuel(self, fuel: int):
        pass


class Car(Vehicle):
    AC_CONSUMPTION = 0.9

    def drive(self, distance: int):
        required_fuel = (self.fuel_consumption + self.AC_CONSUMPTION) * distance
        if self.fuel_quantity >= required_fuel:
            self.fuel_quantity -= required_fuel

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AC_CONSUMPTION = 1.6
    FUEL_COEFFICIENT = 0.95

    def drive(self, distance: int):
        required_fuel = (self.fuel_consumption + self.AC_CONSUMPTION) * distance
        if self.fuel_quantity >= required_fuel:
            self.fuel_quantity -= required_fuel

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel * self.FUEL_COEFFICIENT

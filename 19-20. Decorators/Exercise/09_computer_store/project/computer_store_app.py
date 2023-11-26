from typing import List
from project.computer_types.computer import Computer
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:

    def __init__(self):
        self.warehouse: List[Computer] = []
        self.profits: int = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer == "Desktop Computer":
            computer = DesktopComputer(manufacturer, model)
        elif type_computer == "Laptop":
            computer = Laptop(manufacturer, model)
        else:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        result = computer.configure_computer(processor, ram)
        self.warehouse.append(computer)

        return result

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        computer = next((computer for computer in self.warehouse if computer.processor == wanted_processor and computer.ram >= wanted_ram and computer.price <= client_budget), None)
        if not computer:
            raise Exception(f"Sorry, we don't have a computer for you.")

        self.profits += client_budget - computer.price
        self.warehouse.remove(computer)

        return f"{repr(computer)} sold for {client_budget}$."

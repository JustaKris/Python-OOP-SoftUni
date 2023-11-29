from abc import ABC, abstractmethod
from typing import List
from project.equipment.base_equipment import BaseEquipment


class BaseTeam(ABC):

    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.__name = name
        self.__country = country
        self.__advantage = advantage
        self.budget = budget
        self.wins:int = 0
        self.equipment: List[BaseEquipment] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        pass

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        pass

    @ @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value):
        pass

    @abstractmethod
    def win(self):
        pass

    def get_statistics(self):
        total_price_of_team_equipment = 0  # Todo: this
        avg_team_protection = 0  # Todo: this

        return (f"Name: {self.name}\n"
                f"Country: {self.country}\n"
                f"Advantage: {self.advantage} points\n"
                f"Budget: {self.budget}EUR\n"
                f"Wins: {self.wins}\n"
                f"Total Equipment Price: {total_price_of_team_equipment}\n"
                f"Average Protection: {avg_team_protection}")

from abc import ABC, abstractmethod
from typing import List

from project.fish.base_fish import BaseFish


class BaseDiver(ABC):

    def __init__(self, name: str, oxygen_level: float):
        self.name = name
        self.oxygen_level = oxygen_level  # in seconds
        self.catch: List[BaseFish] = []
        self.competition_points: float = 0
        self.has_health_issue: bool = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Diver name cannot be null or empty!")
        self.__name = value

    @property
    def oxygen_level(self):
        return self.__oxygen_level

    @oxygen_level.setter
    def oxygen_level(self, value: float):
        if value < 0:
            raise ValueError("Cannot create diver with negative oxygen level!")
        self.__oxygen_level = value

    @abstractmethod
    def miss(self, time_to_catch: int):
        pass

    @abstractmethod
    def renew_oxy(self):
        pass

    def hit(self, fish: BaseFish):
        # if self.oxygen_level - fish.time_to_catch < 0:
        #     self.oxygen_level = 0
        #     self.has_health_issue = True
        # else:
        #     self.oxygen_level -= round(fish.time_to_catch * 0.3, 0)
        #     self.competition_points += fish.points
        #     self.catch.append(fish)
        #
        # if self.oxygen_level == 0:
        #     self.has_health_issue = True
        try:
            self.oxygen_level -= fish.time_to_catch
            self.competition_points += round(fish.points, 1)
            self.catch.append(fish)
        except ValueError:
            self.oxygen_level = 0
        # else:
        #     self.competition_points += fish.points
        #     self.catch.append(fish)

        if self.oxygen_level == 0:
            self.has_health_issue = True

    def update_health_status(self):
        self.has_health_issue = not self.has_health_issue

    def __str__(self):
        return (f"{self.__class__.__name__}: [Name: {self.name}, Oxygen level left: {self.oxygen_level}, "
                f"Fish caught: {len(self.catch)}, Points earned: {self.competition_points:.1f}]")

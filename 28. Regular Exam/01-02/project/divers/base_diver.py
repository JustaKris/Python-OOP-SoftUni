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
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if not value.strip():
            raise ValueError("Diver name cannot be null or empty!")
        self.__name = value

    @property
    def oxygen_level(self) -> float:
        return self.__oxygen_level

    @oxygen_level.setter
    def oxygen_level(self, value: float) -> None:
        if value < 0:
            raise ValueError("Cannot create diver with negative oxygen level!")
        self.__oxygen_level = value

    @abstractmethod
    def miss(self, time_to_catch: int) -> None:
        pass

    @abstractmethod
    def renew_oxy(self) -> None:
        pass

    def hit(self, fish: BaseFish) -> None:
        try:
            self.oxygen_level -= fish.time_to_catch
            self.competition_points += round(fish.points, 1)
            self.catch.append(fish)
        except ValueError:
            self.oxygen_level = 0

    def update_health_status(self) -> None:
        self.has_health_issue = not self.has_health_issue

    def __str__(self) -> str:
        return (f"{self.__class__.__name__}: [Name: {self.name}, Oxygen level left: {self.oxygen_level}, "
                f"Fish caught: {len(self.catch)}, Points earned: {self.competition_points:.1f}]")

    # Helper methods
    def oxygen_level_health_issue_check(self) -> None:
        if self.oxygen_level == 0:
            self.update_health_status()

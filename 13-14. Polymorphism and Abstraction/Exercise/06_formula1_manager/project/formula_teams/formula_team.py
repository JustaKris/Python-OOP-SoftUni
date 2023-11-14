from abc import ABC, abstractmethod


class FormulaTeam(ABC):

    def __init__(self, budget: int):
        self.__budget = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value: int):
        if value < 1000000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value

    @abstractmethod
    def get_team_data(self) -> tuple:
        pass

    def calculate_revenue_after_race(self, race_pos: int):
        sponsors, expenses = self.get_team_data()
        revenue = -expenses
        for sponsor in sponsors.values():
            for pos, amount in sponsor.items():
                if pos >= race_pos:
                    revenue += amount
                    break
        self.budget += revenue

        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"

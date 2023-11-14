from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    def __init__(self, budget: int):
        self.__budget = budget
        self.__sponsors: list[dict] = [{}]
        self.__expenses: int = 0

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1000000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value

    @abstractmethod
    def calculate_revenue_after_race(self, race_pos: int):
        pass

    # def calculate_revenue_after_race(self, race_pos: int):
    #     winnings = 0
    #
    #     for sponsor in self.__sponsors:
    #         for pos, amount in sponsor.items():
    #             if pos >= race_pos:
    #                 winnings += amount
    #                 break
    #
    #     revenue = winnings - self.__expenses
    #     self.budget += revenue
    #
    #     return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"

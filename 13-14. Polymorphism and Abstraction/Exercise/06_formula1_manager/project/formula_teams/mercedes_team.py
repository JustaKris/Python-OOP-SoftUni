from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):

    def __init__(self, budget):
        super().__init__(budget)
        self.__sponsors = [{1: 1000000, 3: 500000}, {5: 100000, 7: 50000}]
        self.__expenses = 200000

    def calculate_revenue_after_race(self, race_pos: int):
        winnings = 0

        for sponsor in self.__sponsors:
            for pos, amount in sponsor.items():
                if pos >= race_pos:
                    winnings += amount
                    break

        revenue = winnings - self.__expenses
        self.budget += revenue

        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"


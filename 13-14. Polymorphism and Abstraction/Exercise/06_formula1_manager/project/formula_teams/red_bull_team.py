from formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    def calculate_revenue_after_race(self, race_pos: int):
        # sponsors = {
        #     "Oracle": {
        #         1: 1500000,
        #         2: 800000
        #     },
        #     "Honda": {
        #         8: 20000,
        #         10: 10000
        #     }
        # }
        sponsors = {
            1: 1500000,
            2: 800000,
            8: 20000,
            10: 10000
        }
        expenses = 250000

        revenue = 0
        for pos, amount in sponsors.items():
            if race_pos >= pos:
                revenue = sponsors[race_pos] - expenses
                break
        self.budget += revenue

        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"

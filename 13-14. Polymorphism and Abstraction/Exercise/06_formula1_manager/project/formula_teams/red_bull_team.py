from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    __sponsors = {"Oracle": {1: 1500000, 2: 800000}, "Honda": {8: 20000, 10: 10000}}
    __expenses = 250000

    def get_team_data(self):
        return self.__sponsors, self.__expenses

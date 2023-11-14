from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    __sponsors = {"Petronas": {1: 1000000, 3: 500000}, "TeamViewer": {5: 100000, 7: 50000}}
    __expenses = 200000

    def get_team_data(self):
        return self.__sponsors, self.__expenses

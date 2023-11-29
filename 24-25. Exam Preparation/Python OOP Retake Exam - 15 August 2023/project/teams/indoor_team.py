from project.teams.base_team import BaseTeam


class IndoorTeam(BaseTeam):
    _budget = 500.0

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, self._budget)

    def win(self):
        self.advantage += 145
        self.wins += 1

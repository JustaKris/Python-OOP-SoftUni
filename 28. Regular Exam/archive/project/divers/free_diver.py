from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    INITIAL_OXYGEN_LEVEL = 120

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_OXYGEN_LEVEL)

    def miss(self, time_to_catch: int):
        try:
            self.oxygen_level -= round(time_to_catch * 0.6, 0)
        except ValueError:
            self.oxygen_level = 0

        if self.oxygen_level == 0:
            self.has_health_issue = True

    def renew_oxy(self):
        self.oxygen_level = self.INITIAL_OXYGEN_LEVEL

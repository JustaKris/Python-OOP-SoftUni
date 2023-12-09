from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    INITIAL_OXYGEN_LEVEL = 540

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_OXYGEN_LEVEL)

    def miss(self, time_to_catch: int):
        # if self.oxygen_level - time_to_catch <= 0:
        #     self.oxygen_level = 0
        #     self.has_health_issue = True
        # else:
        #     self.oxygen_level -= round(time_to_catch * 0.3, 0)
        try:
            self.oxygen_level -= round(time_to_catch * 0.3, 0)
        except ValueError:
            self.oxygen_level = 0

        if self.oxygen_level == 0:
            self.has_health_issue = True

    def renew_oxy(self):
        self.oxygen_level = self.INITIAL_OXYGEN_LEVEL

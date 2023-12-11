from typing import List

from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    DIVER_TYPES = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    FISH_TYPES = {"DeepSeaFish": DeepSeaFish, "PredatoryFish": PredatoryFish}

    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str) -> str:
        if diver_type not in self.DIVER_TYPES:
            return f"{diver_type} is not allowed in our competition."

        if diver_name in [d.name for d in self.divers]:
            return f"{diver_name} is already a participant."

        self.divers.append(self.DIVER_TYPES[diver_type](diver_name))

        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float) -> str:
        if fish_type not in self.FISH_TYPES:
            return f"{fish_type} is forbidden for chasing in our competition."

        if fish_name in [f.name for f in self.fish_list]:
            return f"{fish_name} is already permitted."

        self.fish_list.append(self.FISH_TYPES[fish_type](fish_name, points))

        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool) -> str:
        # Diver validation
        diver = next((d for d in self.divers if d.name == diver_name), None)
        if diver is None:
            return f"{diver_name} is not registered for the competition."

        # Fish Validation
        fish = next((f for f in self.fish_list if f.name == fish_name), None)
        if fish is None:
            return f"The {fish_name} is not allowed to be caught in this competition."

        # Diver health check
        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        # Oxygen checks
        if diver.oxygen_level < fish.time_to_catch or diver.oxygen_level == fish.time_to_catch and not is_lucky:
            diver.miss(fish.time_to_catch)
            diver.oxygen_level_health_issue_check()
            return f"{diver_name} missed a good {fish_name}."
        elif diver.oxygen_level == fish.time_to_catch and is_lucky or diver.oxygen_level > fish.time_to_catch:
            diver.hit(fish)
            diver.oxygen_level_health_issue_check()
            return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self) -> str:
        injured_divers_count = len([diver.renew_oxy() or diver.update_health_status() for diver in self.divers if diver.has_health_issue])
        return f"Divers recovered: {injured_divers_count}"

    def diver_catch_report(self, diver_name: str) -> str:
        diver = next((d for d in self.divers if d.name == diver_name), None)
        fish_details = '\n'.join([f.fish_details() for f in diver.catch])
        return f"**{diver_name} Catch Report**\n{fish_details}"

    def competition_statistics(self) -> str:
        sorted_divers = sorted(self.divers, key=lambda d: (-d.competition_points, -len(d.catch), d.name))
        divers_info = '\n'.join([d.__str__() for d in sorted_divers if not d.has_health_issue])
        return f"**Nautical Catch Challenge Statistics**\n{divers_info}"

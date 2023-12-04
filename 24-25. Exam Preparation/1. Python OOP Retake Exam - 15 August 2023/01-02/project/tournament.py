from typing import List

from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    EQUIPMENT_TYPES = {"KneePad": KneePad, "ElbowPad": ElbowPad}
    TEAM_TYPES = {"OutdoorTeam": OutdoorTeam, "IndoorTeam": IndoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.EQUIPMENT_TYPES:
            raise Exception("Invalid equipment type!")
        self.equipment.append(self.EQUIPMENT_TYPES[equipment_type]())
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.TEAM_TYPES:
            raise Exception("Invalid team type!")
        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."
        self.teams.append(self.TEAM_TYPES[team_type](team_name, country, advantage))
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        team = next((t for t in self.teams if t.name == team_name), None)
        equipment = next((e for e in reversed(self.equipment) if type(e).__name__ == equipment_type), None)
        if equipment.price > team.budget:
            raise Exception("Budget is not enough!")
        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = next((t for t in self.teams if t.name == team_name), None)
        if team is None:
            raise Exception("No such team!")
        if team.wins:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")
        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        equipment_to_change = [e for e in self.equipment if type(e).__name__ == equipment_type]
        [e.increase_price() for e in equipment_to_change]
        return f"Successfully changed {len(equipment_to_change)}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = next((team for team in self.teams if team.name == team_name1), None)
        team2 = next((team for team in self.teams if team.name == team_name2), None)

        if team1.__class__.__name__ != team2.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        team1_points, team2_points = self.get_team_points(team1), self.get_team_points(team2)
        winner = team1 if team1_points > team2_points else team2 if team2_points > team1_points else None
        if winner is None:
            return "No winner in this game."
        winner.win()
        return f"The winner is {winner.name}."

    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda t: -t.wins)
        stats = '\n'.join([team.get_statistics() for team in sorted_teams])
        return (f"Tournament: {self.name}\n"
                f"Number of Teams: {len(self.teams)}\n"
                f"Teams:\n"
                f"{stats}")

    # helper methods
    @staticmethod
    def get_team_points(team: BaseTeam):
        team_protection = sum((e.protection for e in team.equipment), 0)
        return team.advantage + team_protection

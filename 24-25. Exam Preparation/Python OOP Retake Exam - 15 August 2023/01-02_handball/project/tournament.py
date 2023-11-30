from typing import List

from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:

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
        if equipment_type == "KneePad":
            self.equipment.append(KneePad())
        elif equipment_type == "ElbowPad":
            self.equipment.append(ElbowPad())
        else:
            raise Exception("Invalid equipment type!")

        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type == "OutdoorTeam":
            team = OutdoorTeam(team_name, country, advantage)
        elif team_type == "IndoorTeam":
            team = IndoorTeam(team_name, country, advantage)
        else:
            raise Exception("Invalid team type!")

        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."

        # if any(t.name == team_name for t in self.teams):
        #     return f"Team with name {team_name} already exists."

        self.teams.append(team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        team = next(t for t in self.teams if t.name == team_name)
        equipment = next((e for e in reversed(self.equipment) if type(e).__name__ == equipment_type), None)

        if equipment.price > team.budget:
            raise Exception("Budget is not enough!")
        
        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price

        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = next(t for t in self.teams if t.name == team_name)

        if not team:
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
        team1 = next(team for team in self.teams if team.name == team_name1)
        team2 = next(team for team in self.teams if team.name == team_name2)

        if type(team1).__name__ != type(team2).__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        team1_points, team2_points = self.get_team_points(team1), self.get_team_points(team2)

        if team1_points > team2_points:
            winner = team1
        elif team1_points < team2_points:
            winner = team2
        else:
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
        team_protection = sum(e.protection for e in team.equipment)
        return team.advantage + team_protection

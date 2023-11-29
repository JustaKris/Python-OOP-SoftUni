from typing import List

from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:

    def __init__(self, name: str, capacity: int):
        self.__name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @@property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        for el in value:
            if not el.isdigit() or not el.isalpha():
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

        if any(t.name == team_name for t in self.teams):
            return f"Team with name {team_name} already exists."

        self.teams.append(team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        team = next(t for t in self.teams if t.name == team_name)
        equipment = next(e for e in self.equipment if type(e) == equipment_type)

        if equipment.price > team.budget:
            raise Exception("Budget is not enough!")

        # team.equipment.append(self.equipment.remove(equipment))
        
        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price

        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        pass

    def increase_equipment_price(self, equipment_type: str):
        pass

    def play(self, team_name1: str, team_name2: str):
        pass

    def get_statistics(self):
        pass

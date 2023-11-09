from typing import List

from project.dvd import DVD


class Customer:
    def __init__(self, name: str, age: int, customer_id: int):
        self.name: str = name
        self.age: int = age
        self.id: int = customer_id
        self.rented_dvds: List[DVD] = []

    def __repr__(self):
        dvd_names = [dvd.name for dvd in self.rented_dvds]
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's ({', '.join(dvd_names)})"

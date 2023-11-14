# from __future__ import annotations

from typing import List


class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __add__(self, other: 'Person'):
        return Person(self.name, other.surname)

    def __repr__(self):
        return f"{self.name} {self.surname}"


class Group:
    def __init__(self, name: str, people: List[Person]):
        self.name = name
        self.people = people

    def __add__(self, other: 'Group'):
        return Group(f"{self.name} {other.name}", self.people + other.people)

    def __len__(self):
        return len(self.people)

    # def __iter__(self):
    #     result = [f"Person {index}: {repr(person)}" for index, person in enumerate(self.people)]
    #     return iter(result)

    def __getitem__(self, index: int):
        return f"Person {index}: {repr(self.people[index])}"

    def __repr__(self):
        return f"Group {self.name} with members {', '.join([repr(person) for person in self.people])}"

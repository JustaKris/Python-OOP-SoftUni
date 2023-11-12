from typing import List


class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __add__(self, other):
        return Person(self.name, other.surname)

    def __repr__(self):
        return f"{self.name} {self.surname}"


class Group:
    def __init__(self, name: str, people: List[Person]):
        self.name = name
        self.people = people

    def __add__(self, other):
        new_group_name = f"{self.name} {other.name}"
        new_group_members = self.people + other.people
        return Group(new_group_name, new_group_members)

    def __len__(self):
        return len(self.people)

    def __iter__(self):
        result = [f"Person {index}: {repr(person)}" for index, person in enumerate(self.people)]
        return iter(result)

    def __getitem__(self, index):
        return f"Person {index}: {repr(self.people[index])}"

    def __repr__(self):
        return f"Group {self.name} with members {', '.join([repr(person) for person in self.people])}"

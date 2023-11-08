from typing import List

from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, worker_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = worker_capacity
        self.animals: List[Lion, Tiger, Cheetah] = []
        self.workers: List[Keeper, Caretaker, Vet] = []

    def add_animal(self, animal: [Lion, Tiger, Cheetah], price: int) -> str:
        if self.__animal_capacity <= 0:
            return "Not enough space for animal"
        elif self.__budget < price:
            return "Not enough budget"
        self.animals.append(animal)
        self.__animal_capacity -= 1
        self.__budget -= price
        return f"{animal.name} the {type(animal).__name__} added to the zoo"

    def hire_worker(self, worker: [Keeper, Caretaker, Vet]) -> str:
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {type(worker).__name__} hired successfully"

    def fire_worker(self, worker_name: str) -> str:
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        total_salaries = sum([worker.salary for worker in self.workers])
        if self.__budget >= total_salaries:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        animal_care_costs = sum([animal.money_for_care for animal in self.animals])
        if self.__budget >= animal_care_costs:
            self.__budget -= animal_care_costs
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        return (
            f"You have {len(self.animals)} animals"
            f"\n----- {self.__class_type_counter(self.animals, Lion)} Lions:\n{self.__class__repr__list(self.animals, Lion)}"
            f"\n----- {self.__class_type_counter(self.animals, Tiger)} Tigers:\n{self.__class__repr__list(self.animals, Tiger)}"
            f"\n----- {self.__class_type_counter(self.animals, Cheetah)} Cheetahs:\n{self.__class__repr__list(self.animals, Cheetah)}"
        )

    def workers_status(self) -> str:
        return (
            f"You have {len(self.workers)} workers"
            f"\n----- {self.__class_type_counter(self.workers, Keeper)} Keepers:\n{self.__class__repr__list(self.workers, Keeper)}"
            f"\n----- {self.__class_type_counter(self.workers, Caretaker)} Caretakers:\n{self.__class__repr__list(self.workers, Caretaker)}"
            f"\n----- {self.__class_type_counter(self.workers, Vet)} Vets:\n{self.__class__repr__list(self.workers, Vet)}"
        )

    @staticmethod
    def __class_type_counter(classes_list: list, class_type: [Lion, Tiger, Cheetah, Keeper, Caretaker, Vet]) -> int:
        return sum([1 for obj in classes_list if isinstance(obj, class_type)])

    @staticmethod
    def __class__repr__list(classes_list: list, class_type: [Lion, Tiger, Cheetah, Keeper, Caretaker, Vet]) -> str:
        return "\n".join(obj.__repr__() for obj in classes_list if isinstance(obj, class_type))

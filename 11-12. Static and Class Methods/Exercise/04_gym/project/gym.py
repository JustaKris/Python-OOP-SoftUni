from typing import List

from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    def add_customer(self, customer: Customer):
        self.customers.append(customer) if customer not in self.customers else None

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        self.plans.append(plan) if plan not in self.plans else None

    def add_subscription(self, subscription: Subscription):
        self.subscriptions.append(subscription) if subscription not in self.subscriptions else None

    def subscription_info(self, subscription_id: int):
        subscription = next(subscription for subscription in self.subscriptions if subscription.id == subscription_id)
        customer = next(customer for customer in self.customers if customer.id == subscription.customer_id)
        trainer = next(trainer for trainer in self.trainers if trainer.id == subscription.trainer_id)
        equipment = next(equipment for equipment in self.equipment if equipment.id == subscription.exercise_id)
        plan = next(plan for plan in self.plans if plan.id == subscription.exercise_id)

        return (
            f"{repr(subscription)}\n"
            f"{repr(customer)}\n"
            f"{repr(trainer)}\n"
            f"{repr(equipment)}\n"
            f"{repr(plan)}"
        )

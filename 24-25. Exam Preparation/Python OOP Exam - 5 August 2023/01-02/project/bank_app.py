from typing import List

from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    LOAN_TYPES = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    CLIENT_TYPES = {"Student": Student, "Adult": Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity  # capacity of clients a bank can have
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.LOAN_TYPES:
            raise ValueError("Invalid loan type!")
        self.loans.append(self.LOAN_TYPES[loan_type]())
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.CLIENT_TYPES:
            raise ValueError("Invalid client type!")
        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."
        self.clients.append(self.CLIENT_TYPES[client_type](client_name, client_id, income))
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        loan = next((l for l in self.loans if type(l).__name__ == loan_type), None)
        client = next((c for c in self.clients if c.client_id == client_id), None)
        if type(loan).__name__ not in client.get_valid_loan_types():
            raise ValueError("Inappropriate loan type!")
        self.loans.remove(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client.client_id}."

    def remove_client(self, client_id: str):
        client = next((c for c in self.clients if c.client_id == client_id), None)
        if not client:
            raise Exception("No such client!")
        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")
        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client.client_id}."

    def increase_loan_interest(self, loan_type: str):
        changed_loans = [l.increase_interest_rate() for l in self.loans if type(l).__name__ == loan_type]
        return f"Successfully changed {len(changed_loans)} loans."

    def increase_clients_interest(self, min_rate: float):
        changed_clients = [c.increase_clients_interest() for c in self.clients if c.interest < min_rate]
        return f"Number of clients affected: {len(changed_clients)}."

    def get_statistics(self):
        total_clients_income = sum(c.income for c in self.clients)
        loans_count_granted_to_clients = sum(len(c.loans) for c in self.clients)
        granted_sum = sum(sum(l.amount for l in c.loans) for c in self.clients)
        not_granted_sum = sum([l.amount for l in self.loans], 0)
        avg_client_interest_rate = sum(c.interest for c in self.clients) / len(self.clients) if self.clients else 0
        result = (f"Active Clients: {len(self.clients)}\n"
                  f"Total Income: {total_clients_income:.2f}\n"
                  f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}\n"
                  f"Available Loans: {len(self.loans)}, Total Sum: {not_granted_sum:.2f}\n"
                  f"Average Client Interest Rate: {avg_client_interest_rate:.2f}")
        return result

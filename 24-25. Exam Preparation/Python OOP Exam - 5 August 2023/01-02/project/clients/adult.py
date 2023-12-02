from project.clients.base_client import BaseClient


class Adult(BaseClient):
    INTEREST = 4.0

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, self.INTEREST)

    def increase_clients_interest(self):
        self.interest += 2.0

    def get_valid_loan_types(self):
        return ['MortgageLoan']

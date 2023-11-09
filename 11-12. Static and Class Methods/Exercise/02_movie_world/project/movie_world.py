import calendar

from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers: list[Customer] = []
        self.dvds: list[DVD] = []

    @property
    def dvd_capacity(self):
        return 15

    @property
    def customer_capacity(self):
        return 10

    def add_customer(self, customer: Customer) -> None:
        if len(self.customers) < self.customer_capacity:
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD) -> None:
        if len(self.dvds) < self.dvd_capacity:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int) -> str:
        for customer in self.customers:
            if customer.id == customer_id:
                # 1.If customer has already rented this dvd
                for dvd in customer.rented_dvds:
                    if dvd.id == dvd_id:
                        return f"{customer.name} has already rented {dvd.name}"  # 1
                # Looping through all dvds
                for dvd in self.dvds:
                    if dvd.id == dvd_id:
                        # 2.If dvd is already rented
                        if dvd.is_rented:
                            return "DVD is already rented"  # 2
                        # 3.If customer is too young to rent this dvd
                        if customer.age < dvd.age_restriction:
                            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"  # 3
                        # 4.Successful rent
                        dvd.is_rented = True
                        customer.rented_dvds.append(dvd)
                        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        for customer in self.customers:
            if customer.id == customer_id:
                for dvd in customer.rented_dvds:
                    if dvd.id == dvd_id:
                        dvd.is_rented = False
                        customer.rented_dvds.remove(dvd)
                        return f"{customer.name} has successfully returned {dvd.name}"
                return f"{customer.name} does not have that DVD"

    def __repr__(self):
        customers_str = "\n".join([repr(customer) for customer in self.customers])
        dvds_str = "\n".join([repr(dvd) for dvd in self.dvds])
        return f"{customers_str}\n{dvds_str}"


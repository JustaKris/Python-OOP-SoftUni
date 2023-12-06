from project.truck_driver import TruckDriver
from unittest import TestCase, main


class TestTruckDriver(TestCase):
    name = 'Hanko Brat'
    money_per_mile = 50.0

    def setUp(self):
        self.truck_driver = TruckDriver(self.name, self.money_per_mile)

    def test_init(self):
        self.assertEqual(self.truck_driver.name, self.name)
        self.assertEqual(self.truck_driver.money_per_mile, self.money_per_mile)
        self.assertEqual(self.truck_driver.available_cargos, {})
        self.assertEqual(self.truck_driver.earned_money, 0)
        self.assertEqual(self.truck_driver.miles, 0)

    def test_earned_money_setter_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.truck_driver.earned_money = -25
        self.assertEqual(str(ex.exception), f"{self.name} went bankrupt.")

    def test_add_cargo(self):
        cargo_location = 'Lapland'
        cargo_miles = 250
        expected_cargos = {cargo_location: cargo_miles}
        result = self.truck_driver.add_cargo_offer(cargo_location, cargo_miles)
        self.assertEqual(result, f"Cargo for {cargo_miles} to {cargo_location} was added as an offer.")
        self.assertEqual(self.truck_driver.available_cargos, expected_cargos)

        # Exception test
        with self.assertRaises(Exception) as ex:
            self.truck_driver.add_cargo_offer(cargo_location, cargo_miles)
        self.assertEqual(str(ex.exception), "Cargo offer is already added.")

    def test_drive_best_cargo_offer(self):
        # No cargo test
        result = self.truck_driver.drive_best_cargo_offer()
        self.assertEqual(result, "There are no offers available.")

        # Proper test
        cargo_location = 'Lapland'
        cargo_miles = 250
        self.truck_driver.add_cargo_offer(cargo_location, cargo_miles)
        self.truck_driver.add_cargo_offer(cargo_location + '2', cargo_miles - 10)
        result = self.truck_driver.drive_best_cargo_offer()

        self.assertEqual(result, f"{self.name} is driving {cargo_miles} to {cargo_location}.")
        self.assertEqual(self.truck_driver.earned_money, self.money_per_mile * cargo_miles - 20)
        self.assertEqual(self.truck_driver.miles, cargo_miles)

    def test_check_for_activities(self):
        self.truck_driver.miles = 10000
        self.truck_driver.earned_money = 15000
        self.truck_driver.check_for_activities(self.truck_driver.miles)
        self.assertEqual(self.truck_driver.earned_money, 3250)

    def test_repr(self):
        miles = 10000
        self.truck_driver.miles += miles
        expected_result = f"{self.name} has {miles} miles behind his back."
        self.assertEqual(repr(self.truck_driver), expected_result)


if __name__ == '__main__':
    main()

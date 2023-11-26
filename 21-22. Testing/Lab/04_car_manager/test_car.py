from car import Car
from unittest import TestCase, main


class TestCar(TestCase):

    def setUp(self):
        self.car = Car("BMW", "M4", 10, 100)

    def test_init(self):
        self.assertEqual("BMW", self.car.make)
        self.assertEqual("M4", self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(100, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_setter_exception(self):
        with self.assertRaises(Exception) as ex:
            car = Car("", "M4", 10, 100)

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_setter_exception(self):
        with self.assertRaises(Exception) as ex:
            car = Car("BMW", "", 10, 100)

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_setter_exception(self):
        with self.assertRaises(Exception) as ex:
            car = Car("BMW", "M4", -10, 100)

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_setter_exception(self):
        with self.assertRaises(Exception) as ex:
            car = Car("BMW", "M4", 10, -100)

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_drive_refuel_and_fuel_amount(self):
        self.car.refuel(75)
        self.assertEqual(75, self.car.fuel_amount)

        self.car.drive(100)
        self.assertEqual(65, self.car.fuel_amount)

    def test_refuel_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_drive_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(1000)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == "__main__":
    main()

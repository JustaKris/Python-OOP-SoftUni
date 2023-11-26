from project.vehicle import Vehicle
from unittest import TestCase, main


class TestCar(TestCase):

    def setUp(self):
        self.vehicle = Vehicle(72.5, 2000)

    def test_init(self):
        self.assertEqual(72.5, self.vehicle.fuel)
        self.assertEqual(72.5, self.vehicle.capacity)
        self.assertEqual(2000, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_and_refuel(self):
        self.vehicle.drive(10)
        self.assertEqual(60, self.vehicle.fuel)

        self.vehicle.refuel(5)
        self.assertEqual(65, self.vehicle.fuel)

    def test_drive_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(500000)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(500000)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test__str__(self):
        expected_value = (f"The vehicle has {self.vehicle.horse_power} horse power with {self.vehicle.fuel}"
                          f" fuel left and {self.vehicle.fuel_consumption} fuel consumption")

        self.assertEqual(expected_value, self.vehicle.__str__())


if __name__ == "__main__":
    main()

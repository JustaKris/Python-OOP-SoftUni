from unittest import TestCase, main
from project.second_hand_car import SecondHandCar


class TestSecondhandCar(TestCase):

    def setUp(self):
        self.bmw = SecondHandCar("BMW M4", "sedan", 1500, 8000)

    def test_init(self):
        self.assertEqual(self.bmw.model, "BMW M4")
        self.assertEqual(self.bmw.car_type, "sedan")
        self.assertEqual(self.bmw.mileage, 1500)
        self.assertEqual(self.bmw.price, 8000)
        self.assertEqual(self.bmw.repairs, [])

    def test_price_setter_exception(self):
        with self.assertRaises(ValueError) as ex:
            car = SecondHandCar("BMW M4", "sedan", 1500, -8000)
        self.assertEqual(str(ex.exception), 'Price should be greater than 1.0!')

    def test_mileage_setter_exception(self):
        with self.assertRaises(ValueError) as ex:
            car = SecondHandCar("BMW M4", "sedan", -1500, 8000)
        self.assertEqual(str(ex.exception), 'Please, second-hand cars only! Mileage must be greater than 100!')

    def test_set_promotional_price(self):
        promo_price = 6000
        result = self.bmw.set_promotional_price(promo_price)
        self.assertEqual(result, 'The promotional price has been successfully set.')
        self.assertEqual(self.bmw.price, promo_price)

    def test_promotional_price_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.bmw.set_promotional_price(25000)
        self.assertEqual(str(ex.exception), 'You are supposed to decrease the price!')

    def test_need_repair(self):
        result = self.bmw.need_repair(1200, "blinkers installation")
        self.assertEqual(result, 'Price has been increased due to repair charges.')
        self.assertEqual(self.bmw.price, 9200)
        self.assertEqual(self.bmw.repairs, ["blinkers installation"])

    def test_need_repairs_too_expensive(self):
        result = self.bmw.need_repair(4800, "blinkers installation x4")
        self.assertEqual(result, 'Repair is impossible!')

    def test_greater(self):
        other_bmw = SecondHandCar("BMW M4", "sedan", 1500, 9000)
        self.assertFalse(self.bmw > other_bmw)

    def test_greater_type_mismatch(self):
        other_bmw = SecondHandCar("BMW M4", "tank", 1500, 9000)
        result = self.bmw > other_bmw
        self.assertEqual(result, 'Cars cannot be compared. Type mismatch!')

    def test_string(self):
        expected_result = (
            'Model BMW M4 | Type sedan | Milage 1500km\n'
            'Current price: 8000.00 | Number of Repairs: 0'
        )
        self.assertEqual(self.bmw.__str__(), expected_result)


if __name__ == '__main__':
    main()

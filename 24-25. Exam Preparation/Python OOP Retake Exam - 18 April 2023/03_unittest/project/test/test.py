from unittest import TestCase, main

from project.robot import Robot


class TestRobot(TestCase):
    robot_id = '80085'
    category = 'Entertainment'
    capacity = 3
    price = 5000.0

    def setUp(self):
        self.robot = Robot(self.robot_id, self.category, self.capacity, self.price)

    def test_init(self):
        self.assertEqual(self.robot.robot_id, self.robot_id)
        self.assertEqual(self.robot.category, self.category)  # aso test setter
        self.assertEqual(self.robot.available_capacity, self.capacity)
        self.assertEqual(self.robot.price, self.price)  # also test setter
        self.assertEqual(self.robot.hardware_upgrades, [])
        self.assertEqual(self.robot.software_updates, [])
        self.assertEqual(self.robot.ALLOWED_CATEGORIES, ['Military', 'Education', 'Entertainment', 'Humanoids'])
        self.assertEqual(self.robot.PRICE_INCREMENT, 1.5)

    def test_category_setter__exception(self):
        with self.assertRaises(ValueError) as ex:
            robot = Robot(self.robot_id, "Philosophy", self.capacity, self.price)
        self.assertEqual(
            str(ex.exception),
            "Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'")

    def test_price_setter__exception(self):
        with self.assertRaises(ValueError) as ex:
            robot = Robot(self.robot_id, self.category, self.capacity, -self.price)
        self.assertEqual(str(ex.exception), "Price cannot be negative!")

    def test_upgrade(self):
        component = "CPU"
        component_price = 2000
        result = self.robot.upgrade(component, component_price)

        self.assertEqual(result, f'Robot {self.robot_id} was upgraded with {component}.')
        self.assertEqual(self.robot.hardware_upgrades, [component])
        self.assertEqual(self.robot.price, 8000)

    def test_upgrade__duplicate_component(self):
        component = "CPU"
        component_price = 2000

        self.robot.upgrade(component, component_price)
        result = self.robot.upgrade(component, component_price)

        self.assertEqual(result, f"Robot {self.robot_id} was not upgraded.")

    def test_update(self):
        version = 1.0
        needed_capacity = 2
        result = self.robot.update(version, needed_capacity)

        self.assertEqual(result, f'Robot {self.robot_id} was updated to version {version}.')
        self.assertEqual(self.robot.software_updates, [version])
        self.assertEqual(self.robot.available_capacity, 1)

    def test_update__lower_version(self):
        version = 1.0
        needed_capacity = 1
        self.robot.update(version, needed_capacity)
        result = self.robot.update(0.5, needed_capacity)

        self.assertEqual(result, f"Robot {self.robot_id} was not updated.")

    def test_update__not_enough_capacity(self):
        version = 1.0
        needed_capacity = 2
        self.robot.update(version, needed_capacity)
        result = self.robot.update(1.5, needed_capacity)

        self.assertEqual(result, f"Robot {self.robot_id} was not updated.")

    def test_greater__cheaper(self):
        other_robot = Robot("Bender", self.category, self.capacity, self.price + 1000)
        result = self.robot > other_robot

        self.assertEqual(result, f'Robot with ID {self.robot_id} is cheaper than Robot with ID {other_robot.robot_id}.')

    def test_greater__more_expensive(self):
        other_robot = Robot("Bender", self.category, self.capacity, self.price - 1000)
        result = self.robot > other_robot

        self.assertEqual(result, f'Robot with ID {self.robot_id} is more expensive than Robot with ID {other_robot.robot_id}.')

    def test_greater__equal(self):
        other_robot = Robot("Bender", self.category, self.capacity, self.price)
        result = self.robot > other_robot

        self.assertEqual(result, f'Robot with ID {self.robot_id} costs equal to Robot with ID {other_robot.robot_id}.')


if __name__ == '__main__':
    main()

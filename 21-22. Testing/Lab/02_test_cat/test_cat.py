from cat import Cat
from unittest import TestCase, main


class CatTest(TestCase):

    def setUp(self):
        self.cat = Cat("Anne Hathaway")

    def test_eat(self):
        expected_size = 1

        self.cat.eat()

        self.assertEqual(expected_size, self.cat.size)
        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)

    def test_eat_when_already_fed(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_sleep(self):
        self.cat.eat()
        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)

    def test_sleeping_cat_when_fed(self):
        self.cat.fed = True

        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)

    def test_sleep_when_hungry(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))


if __name__ == "__main__":
    main()

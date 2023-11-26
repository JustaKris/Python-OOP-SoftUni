from project.mammal import Mammal
from unittest import TestCase, main


class TestCar(TestCase):

    def setUp(self):
        self.mammal = Mammal("Sid", "sloth", "MAANIII")

    def test_init(self):
        self.assertEqual("Sid", self.mammal.name)
        self.assertEqual("sloth", self.mammal.type)
        self.assertEqual("MAANIII", self.mammal.sound)

    def test_make_sound(self):
        self.assertEqual(f"{self.mammal.name} makes {self.mammal.sound}", self.mammal.make_sound())

    def test_kingdom_getter(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info(self):
        self.assertEqual(f"{self.mammal.name} is of type {self.mammal.type}", self.mammal.info())


if __name__ == "__main__":
    main()


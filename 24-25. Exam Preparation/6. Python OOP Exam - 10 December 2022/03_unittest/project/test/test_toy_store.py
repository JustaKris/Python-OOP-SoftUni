from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):
    toy_shelf = {
        "A": None,
        "B": None,
        "C": None,
        "D": None,
        "E": None,
        "F": None,
        "G": None,
    }
    test_shelf = "C"
    test_toy_name = "Rubik's cube"

    def setUp(self):
        self.toy_store = ToyStore()

    def test_init(self):
        self.assertEqual(self.toy_store.toy_shelf, self.toy_shelf)

    def test_add_tpy(self):
        result = self.toy_store.add_toy(self.test_shelf, self.test_toy_name)
        self.assertEqual(result, f"Toy:{self.test_toy_name} placed successfully!")
        self.assertEqual(self.toy_store.toy_shelf["C"], self.test_toy_name)

        # Exception 1
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("Z", self.test_toy_name)
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

        # Exception 2
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy(self.test_shelf, self.test_toy_name)
        self.assertEqual(str(ex.exception), "Toy is already in shelf!")

        # Exception 3
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy(self.test_shelf, "Some other toy")
        self.assertEqual(str(ex.exception), "Shelf is already taken!")

    def test_remove_toy(self):
        self.toy_store.add_toy(self.test_shelf, self.test_toy_name)
        result = self.toy_store.remove_toy(self.test_shelf, self.test_toy_name)
        self.assertEqual(result, f"Remove toy:{self.test_toy_name} successfully!")
        self.assertEqual(self.toy_store.toy_shelf[self.test_shelf], None)

        # Exception 1
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("Z", self.test_toy_name)
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

        # Exception 2
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy(self.test_shelf, self.test_toy_name)
        self.assertEqual(str(ex.exception), "Toy in that shelf doesn't exists!")


if __name__ == '__main__':
    main()

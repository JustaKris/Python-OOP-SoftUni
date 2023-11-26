from integer_list import IntegerList
from unittest import TestCase, main


class TestIntegerList(TestCase):

    def setUp(self):
        self.integer_list = IntegerList(
            '50',
            1,
            False,
            3.5,
            2,
            3
        )

    def test_init_and_get_data(self):
        self.assertEqual([1, 2, 3], self.integer_list.get_data())

    def test_add(self):
        expected_data = self.integer_list.get_data() + [5]
        self.integer_list.add(5)

        self.assertEqual(expected_data, self.integer_list.get_data())

    def test_add_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.integer_list.add("booo!")

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_remove_index(self):
        expected_value = [1, 2]
        self.integer_list.remove_index(2)

        self.assertEqual(expected_value, self.integer_list.get_data())

    def test_remove_index_exception(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.remove_index(27)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get(self):
        self.assertEqual(2, self.integer_list.get(1))

    def test_get_exception(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.get(27)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert(self):
        self.integer_list.insert(1, 255)
        self.assertEqual([1, 255, 2, 3], self.integer_list.get_data())

    def test_insert_exception_index_error(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.insert(27, 255)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_exception_not_int(self):
        with self.assertRaises(ValueError) as ex:
            self.integer_list.insert(1, "255")

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_get_biggest(self):
        self.assertEqual(3, self.integer_list.get_biggest())

    def test_get_index(self):
        self.assertEqual(0, self.integer_list.get_index(1))


if __name__ == "__main__":
    main()

from unittest import TestCase, main

from hash_table import HashTable


class TestHashTable(TestCase):

    def setUp(self):
        self.hash_table = HashTable(100)
        self.hash_table["hello"] = "Hello World!"
        self.hash_table[98.6] = 37
        self.hash_table[False] = True

    def test_init(self):
        self.assertEqual(len(self.hash_table.array), 3)

    def test_create_empty_pair_slots(self):
        hash_table = HashTable(4)
        expected = [None, None, None, None]
        actual = hash_table._array
        self.assertEqual(expected, actual)

    def test_insert_key_value_pair(self):
        hash_table = HashTable(4)
        hash_table["hello"] = "Hello World!"

        self. assertIn(("hello", "Hello World!"), hash_table.array)

    def test_find_value_by_key(self):
        self.assertEqual("Hello World!", self.hash_table["hello"])
        self.assertEqual(37, self.hash_table[98.6])

    def test_str(self):
        actual = str(self.hash_table)
        expected = "{False: True, 98.6: 37, 'hello': 'Hello World!'}"
        self.assertEqual(actual, expected)

    def test_delitem(self):
        self.hash_table.__delitem__("hello")
        self.assertNotIn("hello", self.hash_table.keys)


if __name__ == '__main__':
    main()

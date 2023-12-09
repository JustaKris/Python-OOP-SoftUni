from collections import deque
from unittest import TestCase, main
from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):
    name = "Българска Държавна Железария"

    def setUp(self):
        self.rs = RailwayStation(self.name)

    def test_init(self):
        self.assertEqual(self.rs.name, self.name)
        self.assertEqual(self.rs.arrival_trains, deque())
        self.assertEqual(self.rs.departure_trains, deque())

    def test_name_setter_exception(self):
        with self.assertRaises(ValueError) as ex:
            _ = RailwayStation("BD")
        self.assertEqual(str(ex.exception), "Name should be more than 3 symbols!")

    def test_new_arrival_on_board(self):
        self.rs.new_arrival_on_board("T1")
        self.rs.new_arrival_on_board("T2")
        self.assertEqual(self.rs.arrival_trains, deque(['T1', 'T2']))

    def test_train_has_arrived(self):
        train_info = "T1 to Sofia"
        train_info2 = "T2 to Mordor"
        self.rs.new_arrival_on_board(train_info)
        self.rs.new_arrival_on_board(train_info2)
        self.assertEqual(self.rs.arrival_trains, deque([train_info, train_info2]))
        self.assertEqual(self.rs.departure_trains, deque())

        result = self.rs.train_has_arrived(train_info)
        self.assertEqual(result, f"{train_info} is on the platform and will leave in 5 minutes.")
        self.assertEqual(self.rs.departure_trains, deque([train_info]))
        # self.assertEqual(self.rs.arrival_trains, deque([train_info2]))

    def test_train_has_arrived_wrong_train_departure(self):
        train_info = "T1 to Sofia"
        train_info2 = "T2 to Mordor"
        self.rs.new_arrival_on_board(train_info)
        self.rs.new_arrival_on_board(train_info2)
        result = self.rs.train_has_arrived(train_info2)
        self.assertEqual(result, f"There are other trains to arrive before {train_info2}.")

    def test_train_has_left_true(self):
        train_info = "T1 to Sofia"
        train_info2 = "T2 to Mordor"

        self.rs.new_arrival_on_board(train_info)
        self.rs.new_arrival_on_board(train_info2)
        self.assertEqual(self.rs.arrival_trains, deque([train_info, train_info2]))

        self.rs.train_has_arrived(train_info)
        self.rs.train_has_arrived(train_info2)
        self.assertEqual(self.rs.arrival_trains, deque())
        self.assertEqual(self.rs.departure_trains, deque([train_info, train_info2]))

        result = self.rs.train_has_left(train_info)
        self.assertTrue(result)
        self.assertEqual(self.rs.departure_trains, deque([train_info2]))

    def test_train_has_left_false(self):
        train_info = "T1 to Sofia"
        train_info2 = "T2 to Mordor"
        self.rs.new_arrival_on_board(train_info)
        self.rs.new_arrival_on_board(train_info2)
        self.assertEqual(self.rs.arrival_trains, deque([train_info, train_info2]))

        self.rs.train_has_arrived(train_info)
        self.rs.train_has_arrived(train_info2)
        self.assertEqual(self.rs.arrival_trains, deque())
        self.assertEqual(self.rs.departure_trains, deque([train_info, train_info2]))

        result = self.rs.train_has_left(train_info2)
        self.assertFalse(result)
        self.assertEqual(self.rs.departure_trains, deque([train_info, train_info2]))


if __name__ == '__main__':
    main()

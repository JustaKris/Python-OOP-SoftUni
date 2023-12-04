from project.trip import Trip

from unittest import TestCase, main


class TestTrip(TestCase):

    def setUp(self):
        self.family_trip = Trip(25000, 2, True)
        self.solo_trip = Trip(6500, 1, False)
        self.mislabeled_solo_trip = Trip(6500, 1, True)

    def test_init(self):
        # Family
        self.assertEqual(self.family_trip.budget, 25000)
        self.assertEqual(self.family_trip.travelers, 2)
        self.assertTrue(self.family_trip.is_family)
        self.assertEqual(self.family_trip.booked_destinations_paid_amounts, {})

        # Solo
        self.assertEqual(self.solo_trip.budget, 6500)
        self.assertEqual(self.solo_trip.travelers, 1)
        self.assertFalse(self.solo_trip.is_family)
        self.assertEqual(self.solo_trip.booked_destinations_paid_amounts, {})

        # Mislabeled solo
        self.assertEqual(self.mislabeled_solo_trip.budget, 6500)
        self.assertEqual(self.mislabeled_solo_trip.travelers, 1)
        self.assertFalse(self.mislabeled_solo_trip.is_family)  # test is_family setter
        self.assertEqual(self.mislabeled_solo_trip.booked_destinations_paid_amounts, {})

    def test_travelers_setter_exception(self):
        with self.assertRaises(ValueError) as ex:
            _ = Trip(6500, 0, False)
        self.assertEqual(str(ex.exception), 'At least one traveler is required!')

    def test_book_a_trip(self):
        expected_dict = {'New Zealand': 15000 * 0.9}
        expected_budget = 11500.00
        result = self.family_trip.book_a_trip('New Zealand')

        self.assertEqual(result, f'Successfully booked destination New Zealand! Your budget left is {expected_budget:.2f}')
        self.assertEqual(self.family_trip.booked_destinations_paid_amounts, expected_dict)
        self.assertEqual(self.family_trip.budget, expected_budget)

    def test_book_a_trip_not_enough_budget(self):
        result = self.solo_trip.book_a_trip('New Zealand')
        self.assertEqual(result, 'Your budget is not enough!')

    def test_book_a_trip_wrong_destination(self):
        result = self.solo_trip.book_a_trip('Mordor')
        self.assertEqual(result, 'This destination is not in our offers, please choose a new one!')

    def test_booking_status(self):
        self.family_trip.book_a_trip('New Zealand')
        expected_result = ('Booked Destination: New Zealand\n'
                           'Paid Amount: 13500.00\n'
                           'Number of Travelers: 2\n'
                           'Budget Left: 11500.00')
        result = self.family_trip.booking_status()
        self.assertEqual(result, expected_result)

    def test_booking_status_empty(self):
        result = self.mislabeled_solo_trip.booking_status()
        self.assertEqual(result, f'No bookings yet. Budget: 6500.00')

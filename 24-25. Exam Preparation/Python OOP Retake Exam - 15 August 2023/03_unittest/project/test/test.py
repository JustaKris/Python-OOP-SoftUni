from project.trip import Trip

from unittest import TestCase, main


class TestTrip(TestCase):
    budget = 250
    travelers_number = 3
    is_family = True

    def setUp(self):
        family_trip = Trip(self.budget, self.travelers_number, self.is_family)
        solo_trip = Trip(self.budget, 1, False)


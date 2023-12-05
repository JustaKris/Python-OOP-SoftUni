from unittest import TestCase, main
from project.tennis_player import TennisPlayer


class TestTennisPlayer(TestCase):
    name = "Hanko Brat"
    age = 33
    points = 25

    def setUp(self):
        self.tennis_player = TennisPlayer(self.name, self.age, self.points)

    def test_init(self):
        self.assertEqual(self.tennis_player.name, self.name)
        self.assertEqual(self.tennis_player.age, self.age)
        self.assertEqual(self.tennis_player.points, self.points)
        self.assertEqual(self.tennis_player.wins, [])

    def test_name_setter_error(self):
        with self.assertRaises(ValueError) as ex:
            tennis_player = TennisPlayer("HB", self.age, self.points)
        self.assertEqual(str(ex.exception), "Name should be more than 2 symbols!")

    def test_age_setter_exception(self):
        with self.assertRaises(ValueError) as ex:
            tennis_player = TennisPlayer(self.name, -42, self.points)
        self.assertEqual(str(ex.exception), "Players must be at least 18 years of age!")

    def test_add_new_wins(self):
        tournament_name = "Softuniada"
        self.tennis_player.add_new_win(tournament_name)
        self.assertEqual(self.tennis_player.wins, [tournament_name])

        # Exception test
        result = self.tennis_player.add_new_win(tournament_name)
        self.assertEqual(result, f"{tournament_name} has been already added to the list of wins!")

    def test_less_than(self):
        other_tennis_player = TennisPlayer("Bratko Han", self.age, 1000)
        self.assertEqual(
            first=self.tennis_player < other_tennis_player,
            second=f'{other_tennis_player.name} is a top seeded player and he/she is better than {self.tennis_player.name}')

        other_tennis_player.points = 0
        self.assertEqual(
            first=self.tennis_player < other_tennis_player,
            second=f'{self.tennis_player.name} is a better player than {other_tennis_player.name}')

    def test_str(self):
        tournaments = ["SoftUniada23", "SoftUniada22"]
        [self.tennis_player.add_new_win(tournament) for tournament in tournaments]
        expected_result = (f"Tennis Player: {self.name}\n"
                           f"Age: {self.age}\n"
                           f"Points: {self.points:.1f}\n"
                           f"Tournaments won: {', '.join(tournaments)}")
        self.assertEqual(self.tennis_player.__str__(), expected_result)


if __name__ == '__main__':
    main()

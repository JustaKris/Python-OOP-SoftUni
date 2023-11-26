from project.hero import Hero
from unittest import TestCase, main


class TestCar(TestCase):

    def setUp(self):
        self.hero = Hero("Leeroy", 7, 30, 3)
        self.enemy_hero = Hero("Toshonator", 5, 23, 2)

    def test_init(self):
        self.assertEquals("Leeroy", self.hero.username)
        self.assertEquals(7, self.hero.level)
        self.assertEquals(30, self.hero.health)
        self.assertEquals(3, self.hero.damage)

    def test_battle_loss(self):
        self.assertEqual("You lose", self.hero.battle(self.enemy_hero))
        # self.hero.battle(self.enemy_hero)
        self.assertEqual(20, self.hero.health)
        self.assertEquals(7, self.enemy_hero.health)
        self.assertEquals(6, self.enemy_hero.level)
        self.assertEquals(7, self.enemy_hero.damage)

    def test_battle_win(self):
        self.hero.damage = 25
        self.assertEqual("You win", self.hero.battle(self.enemy_hero))
        self.assertEquals(8, self.hero.level)
        self.assertEquals(25, self.hero.health)
        self.assertEquals(30, self.hero.damage)

    def test_battle_draw(self):
        self.hero.damage = 25
        self.enemy_hero.damage = 25
        self.assertEqual("Draw", self.hero.battle(self.enemy_hero))

    def test_battle_exception_fight_self(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_exception_too_low_health(self):
        self.hero.health = -25
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_exception_enemy_too_low_health(self):
        self.enemy_hero.health = -25
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)

        self.assertEqual(f"You cannot fight {self.enemy_hero.username}. He needs to rest", str(ex.exception))

    def test__str__(self):
        expected_result = (f"Hero {self.hero.username}: {self.hero.level} lvl\n"
                           f"Health: {self.hero.health}\n"
                           f"Damage: {self.hero.damage}\n")
        self.assertEqual(expected_result, self.hero.__str__())


if __name__ == "__main__":
    main()

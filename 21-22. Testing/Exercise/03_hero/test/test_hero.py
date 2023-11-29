from project.hero import Hero
from unittest import TestCase, main


class HeroTest(TestCase):
    # Hero inputs
    username = "Leeroy"
    level = 7
    health = 29.5
    damage = 2.5

    # Enemy hero inputs
    enemy_username = "Toshonator"
    enemy_level = 5
    enemy_health = 22.5
    enemy_damage = 1.8

    def setUp(self):
        self.hero = Hero(self.username, self.level, self.health, self.damage)
        self.enemy_hero = Hero(self.enemy_username, self.enemy_level, self.enemy_health, self.enemy_damage)

    def test_init(self):
        self.assertEqual(self.username, self.hero.username)
        self.assertEqual(self.level, self.hero.level)
        self.assertEqual(self.health, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)

    def test__attribute_types(self):
        self.assertIsInstance(self.username, str)
        self.assertIsInstance(self.level, int)
        self.assertIsInstance(self.health, float)
        self.assertIsInstance(self.damage, float)

    def test_battle_loss(self):
        self.enemy_hero.level, self.enemy_hero.health, self.enemy_hero.damage = [100, 100, 100]

        result = self.hero.battle(self.enemy_hero)

        self.assertEqual("You lose", result)
        self.assertEqual(-9970.5, self.hero.health)
        self.assertEqual(87.5, self.enemy_hero.health)
        self.assertEqual(101, self.enemy_hero.level)
        self.assertEqual(105, self.enemy_hero.damage)

    def test_battle_win(self):
        self.hero.damage = 25
        result = self.hero.battle(self.enemy_hero)

        self.assertEqual("You win", result)
        self.assertEqual(self.level + 1, self.hero.level)
        self.assertEqual(25.5, self.hero.health)
        self.assertEqual(30, self.hero.damage)

        self.assertEqual(5, self.enemy_hero.level)
        self.assertEqual(-152.5, self.enemy_hero.health)
        self.assertEqual(1.8, self.enemy_hero.damage)

    def test_battle_draw(self):
        self.hero.damage = 25
        self.enemy_hero.damage = 25

        expected_hero_health = self.hero.health - (self.enemy_hero.damage * self.enemy_hero.level)
        expected_enemy_hero_health = self.enemy_hero.health - (self.hero.damage * self.hero.level)

        result = self.hero.battle(self.enemy_hero)

        self.assertEqual("Draw", result)
        self.assertEqual(expected_hero_health, self.hero.health)
        self.assertEqual(self.level, self.hero.level)
        self.assertEqual(expected_enemy_hero_health, self.enemy_hero.health)
        self.assertEqual(5, self.enemy_hero.level)

    def test_battle_exception_fight_self(self):
        enemy_hero = Hero(self.username, self.level, self.health, self.damage)

        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_exception_too_low_health(self):
        # Health is zero
        self.hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

        # Health is negative
        self.hero.health -= 25
        with self.assertRaises(ValueError) as ex2:
            self.hero.battle(self.enemy_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex2.exception))

    def test_battle_exception_enemy_too_low_health(self):
        self.enemy_hero.health = -25
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)

        self.assertEqual(f"You cannot fight Toshonator. He needs to rest", str(ex.exception))

    def test__str__(self):
        expected_result = (f"Hero {self.username}: {self.level} lvl\n"
                           f"Health: {self.health}\n"
                           f"Damage: {self.damage}\n")
        self.assertEqual(expected_result, str(self.hero))


if __name__ == "__main__":
    main()

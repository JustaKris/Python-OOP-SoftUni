from project.hero import Hero
from unittest import TestCase, main


class HeroTest(TestCase):
    # Hero inputs
    username = "Leeroy"
    level = 7
    health = 29.5
    damage = 2.5

    def setUp(self):
        self.hero = Hero(self.username, self.level, self.health, self.damage)
        self.enemy_hero = Hero("Toshonator", 5, 22.5, 1.8)

    def test_init(self):
        self.assertEquals(self.username, self.hero.username)
        self.assertEquals(self.level, self.hero.level)
        self.assertEquals(self.health, self.hero.health)
        self.assertEquals(self.damage, self.hero.damage)

    def test__attribute_types(self):
        self.assertIsInstance(self.username, str)
        self.assertIsInstance(self.level, int)
        self.assertIsInstance(self.health, float)
        self.assertIsInstance(self.damage, float)

    def test_battle_loss(self):
        self.hero.health = 10
        self.hero.damage = 10
        enemy_hero = Hero("Toshonator", 100, 100, 100)

        result = self.hero.battle(enemy_hero)

        self.assertEqual("You lose", result)
        self.assertEqual(-9990, self.hero.health)
        self.assertEquals(35, enemy_hero.health)
        self.assertEquals(101, enemy_hero.level)
        self.assertEquals(105, enemy_hero.damage)

    def test_battle_win(self):
        self.hero.damage = 25
        result = self.hero.battle(self.enemy_hero)

        self.assertEqual("You win", result)
        self.assertEquals(self.level + 1, self.hero.level)
        self.assertEquals(25.5, self.hero.health)
        self.assertEquals(30, self.hero.damage)

        self.assertEquals(5, self.enemy_hero.level)
        self.assertEquals(-152.5, self.enemy_hero.health)
        self.assertEquals(1.8, self.enemy_hero.damage)

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

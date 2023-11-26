from worker import Worker
from unittest import TestCase, main


class WorkerTest(TestCase):

    def setUp(self):
        self.worker = Worker("Test Worker", 25000, 100)

    def test_correct_initialization(self):
        self.assertEqual(self.worker.name, "Test Worker")
        self.assertEqual(self.worker.salary, 25000)
        self.assertEqual(self.worker.energy, 100)
        self.assertEqual(self.worker.money, 0)

    def test_work_when_worker_has_energy_expect_money_increase(self):
        expected_energy = self.worker.energy - 2
        expected_money = self.worker.salary * 2

        self.worker.work()
        self.worker.work()

        self.assertEqual(expected_energy, self.worker.energy)
        self.assertEqual(expected_money, self.worker.money)

    def test_work_when_worked_does_not_have_energy_raises_exception(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_increment_energy_with_one_when_resting(self):
        expected_energy = self.worker.energy + 1

        self.worker.rest()

        self.assertEqual(expected_energy, self.worker.energy)

    def test_get_info_returns_valid_string(self):
        self.assertEqual(f'{self.worker.name} has saved {self.worker.money} money.', self.worker.get_info())


if __name__ == '__main__':
    main()

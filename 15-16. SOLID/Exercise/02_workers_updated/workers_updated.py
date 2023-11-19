from abc import ABC, ABCMeta, abstractmethod
import time


class Work(ABC):

    @staticmethod
    @abstractmethod
    def work():
        pass


class Eat(ABC):

    @staticmethod
    @abstractmethod
    def eat():
        pass


class Worker(Work, Eat):

    @staticmethod
    def work():
        print("I'm normal worker. I'm working.")

    @staticmethod
    def eat():
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(Work, Eat):

    @staticmethod
    def work():
        print("I'm super worker. I work very hard!")

    @staticmethod
    def eat():
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Robot(Work):

    @staticmethod
    def work():
        print("I'm a robot. I'm working....")


class Manager(ABC):

    def __init__(self):
        self.worker = None

    @abstractmethod
    def set_worker(self, worker: Work):
        pass


class WorkManager(Manager):

    def set_worker(self, worker: Work):
        assert isinstance(worker, Work), "`worker` must be of type {}".format(Work)

        self.worker = worker

    def manage(self):
        self.worker.work()


class BreakManager(Manager):

    def set_worker(self, worker: Eat):
        assert isinstance(worker, Eat), "`worker` must be of type {}".format(Eat)

        self.worker = worker

    def lunch_break(self):
        self.worker.eat()


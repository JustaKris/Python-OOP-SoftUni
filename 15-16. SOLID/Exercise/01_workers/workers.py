class Worker:

    @staticmethod
    def work():
        print("I'm working!!")


class SuperWorker(Worker):

    @staticmethod
    def work():
        print("I work very hard!!!")


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, Worker), '`worker` must be of type {}'.format(Worker)

        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()

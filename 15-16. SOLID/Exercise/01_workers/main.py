from workers import Worker, SuperWorker, Manager


def main():
    worker = Worker()
    manager = Manager()
    manager.set_worker(worker)
    manager.manage()
    super_worker = SuperWorker()
    try:
        manager.set_worker(super_worker)
        manager.manage()
    except AssertionError:
        print("manager fails to support super_worker....")


if __name__ == '__main__':
    main()

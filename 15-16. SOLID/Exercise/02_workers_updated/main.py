from workers_updated import Worker, SuperWorker, WorkManager, BreakManager, Robot


def main():
    work_manager = WorkManager()
    break_manager = BreakManager()
    work_manager.set_worker(Worker())
    break_manager.set_worker(Worker())
    work_manager.manage()
    break_manager.lunch_break()
    work_manager.set_worker(SuperWorker())
    break_manager.set_worker(SuperWorker())
    work_manager.manage()
    break_manager.lunch_break()
    work_manager.set_worker(Robot())
    work_manager.manage()
    try:
        break_manager.set_worker(Robot())
        break_manager.lunch_break()
    except:
        pass


if __name__ == '__main__':
    main()

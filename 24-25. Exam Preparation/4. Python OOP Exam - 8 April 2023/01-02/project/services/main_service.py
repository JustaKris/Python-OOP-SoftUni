from project.services.base_service import BaseService


class MainService(BaseService):
    CAPACITY = 30

    def __init__(self, name: str):
        super().__init__(name, self.CAPACITY)

    def details(self):
        robots_string = ' '.join([r.name for r in self.robots]) if self.robots else 'none'
        return f"{self.name} Main Service:\nRobots: {robots_string}"

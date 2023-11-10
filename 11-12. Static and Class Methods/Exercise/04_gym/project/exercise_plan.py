class ExercisePlan:
    id = 1

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration  # In minutes
        self.id = self.get_next_id()

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
        return cls(trainer_id, equipment_id, hours * 60)

    @classmethod
    def get_next_id(cls):
        next_id = cls.id
        cls.id += 1
        return next_id

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"

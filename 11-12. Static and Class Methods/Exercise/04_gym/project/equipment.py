class Equipment:
    id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Equipment.get_next_id()

    @classmethod
    def get_next_id(cls):
        next_id = cls.id
        cls.id += 1
        return next_id

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

    # @staticmethod
    # def get_next_id():
    #     return Equipment.id

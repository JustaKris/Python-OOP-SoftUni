class Person:

    def __init__(self, position):
        self.position = position


class FreePerson(Person):

    def walk_north(self, dist: int):
        self.position[1] += dist

    def walk_east(self, dist: int):
        self.position[0] += dist


class Prisoner(Person):
    PRISON_LOCATION = (3, 3)

    def __init__(self):
        super().__init__(self.PRISON_LOCATION)
        self.is_free = False

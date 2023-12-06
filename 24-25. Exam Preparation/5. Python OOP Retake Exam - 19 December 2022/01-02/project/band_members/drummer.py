from project.band_members.musician import Musician


class Drummer(Musician):
    def get_valid_skills(self) -> list:
        return ["play the drums with drumsticks", "play the drums with drum brushes", "read sheet music"]

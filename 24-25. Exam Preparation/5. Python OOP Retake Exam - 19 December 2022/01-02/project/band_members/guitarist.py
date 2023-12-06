from project.band_members.musician import Musician


class Guitarist(Musician):
    def get_valid_skills(self) -> list:
        return ["play metal", "play rock", "play jazz"]

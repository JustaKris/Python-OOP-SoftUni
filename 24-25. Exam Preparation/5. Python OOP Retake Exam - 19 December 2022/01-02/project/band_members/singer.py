from project.band_members.musician import Musician


class Singer(Musician):
    def get_valid_skills(self) -> list:
        return ["sing high pitch notes", "sing low pitch notes"]

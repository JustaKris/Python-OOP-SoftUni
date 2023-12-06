from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert
from project.band_members.musician import Musician


class ConcertTrackerApp:
    VALID_MUSICIAN_TYPES = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}
    CONCERT_REQUIREMENTS_PER_GENRE = {
            "Rock": {
                "Drummer": ["play the drums with drumsticks"],
                "Singer": ["sing high pitch notes"],
                "Guitarist": ["play rock"]
            },
            "Metal": {
                "Drummer": ["play the drums with drumsticks"],
                "Singer": ["sing low pitch notes"],
                "Guitarist": ["play metal"]
            },
            "Jazz": {
                "Drummer": ["play the drums with drum brushes"],
                "Singer": ["sing high pitch notes", "sing low pitch notes"],
                "Guitarist": ["play jazz"]
            }
        }

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIAN_TYPES:
            raise ValueError("Invalid musician type!")
        if name in [m.name for m in self.musicians]:
            raise Exception(f"{name} is already a musician!")
        self.musicians.append(self.VALID_MUSICIAN_TYPES[musician_type](name, age))
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if name in [b.name for b in self.bands]:
            raise Exception(f"{name} band is already created!")
        new_band = Band(name)
        self.bands.append(new_band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        if place in [c.place for c in self.concerts]:
            raise Exception(f"{place} is already registered for {genre} concert!")
        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = next((m for m in self.musicians if m.name == musician_name), None)
        if musician is None:
            raise Exception(f"{musician_name} isn't a musician!")
        band = next((b for b in self.bands if b.name == band_name), None)
        if band is None:
            raise Exception(f"{band_name} isn't a band!")
        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = next((b for b in self.bands if b.name == band_name), None)
        if band is None:
            raise Exception(f"{band_name} isn't a band!")
        if musician_name not in [m.name for m in band.members]:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")
        musician = next((m for m in self.musicians if m.name == musician_name), None)
        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        concert = next((c for c in self.concerts if c.place == concert_place), None)
        band = next((b for b in self.bands if b.name == band_name), None)
        if len(set([m.__class__.__name__ for m in band.members])) < 3:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")
        for musician in band.members:
            for required_skill in self.CONCERT_REQUIREMENTS_PER_GENRE[concert.genre][musician.__class__.__name__]:
                if required_skill not in musician.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."

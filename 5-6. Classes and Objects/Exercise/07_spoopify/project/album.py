from typing import List
from project.song import Song


class Album:
    def __init__(self, name: str, *songs):
        self.name = name
        self.songs: List[Song] = []
        self.published = False

        for song in songs:
            self.songs.append(song)

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        elif self.published:
            return "Cannot add songs. Album is published."
        elif song.name in [s.name for s in self.songs]:
            return "Song is already in the album."
        else:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."
        elif song_name not in [s.name for s in self.songs]:
            return "Song is not in the album."
        else:
            for song in self.songs:
                if song.name == song_name:
                    self.songs.remove(song)
                    return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = f"Album {self.name}\n"
        #  + "\n".join(song.get_info() for song in self.songs) + "\n"
        for song in self.songs:
            result += f"== {song.get_info()}\n"
        return result

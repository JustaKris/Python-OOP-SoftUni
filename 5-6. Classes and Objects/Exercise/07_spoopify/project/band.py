from typing import List
from project.song import Song
from project.album import Album


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums: List[Album] = []

    def add_album(self, album: Album):
        if album.name in [a.name for a in self.albums]:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        if album_name not in [a.name for a in self.albums]:
            return f"Album {album_name} is not found."
        for album_obj in self.albums:
            if album_obj.published:
                return "Album has been published. It cannot be removed."
            self.albums.remove(album_obj)
            return f"Album {album_name} has been removed."

    def details(self):
        return f"Band {self.name}\n" + "\n".join([album.details() for album in self.albums])


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())

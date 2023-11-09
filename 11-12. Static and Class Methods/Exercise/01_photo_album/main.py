from photo_album import PhotoAlbum


def main():
    album = PhotoAlbum(2)
    print(album.add_photo("baby"))
    print(album.add_photo("first grade"))
    print(album.add_photo("eight grade"))
    print(album.add_photo("party with friends"))
    print(album.photos)
    print(album.add_photo("prom"))
    print(album.add_photo("wedding"))
    print(album.display())


if __name__ == "__main__":
    main()

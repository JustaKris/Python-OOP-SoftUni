from playing import start_playing, Children, Guitar


def main():
    guitar = Guitar()
    print(start_playing(guitar))

    children = Children()
    print(start_playing(children))


if __name__ == '__main__':
    main()

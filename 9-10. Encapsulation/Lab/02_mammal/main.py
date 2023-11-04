from mammal import Mammal


def main():
    mammal = Mammal("Dog", "Domestic", "Bark")
    print(mammal.make_sound())
    print(mammal.get_kingdom())
    print(mammal.info())


if __name__ == "__main__":
    main()

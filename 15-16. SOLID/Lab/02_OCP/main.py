from animal import Cat, Dog, Turtle


def main():
    def animal_sound(animals: list) -> None:
        for animal in animals:
            print(animal.make_sound())

    animals = [Cat(), Dog(), Turtle()]
    animal_sound(animals)

    # print(Cat().species)


if __name__ == '__main__':
    main()

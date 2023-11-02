# from project.animal import Animal
from project.dog import Dog


def main():
    doggy = Dog()
    print(doggy.bark())
    print(doggy.eat())


if __name__ == "__main__":
    main()

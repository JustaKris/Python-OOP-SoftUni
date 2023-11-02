from project.cat import Cat
from project.dog import Dog


def main():
    cat = Cat()
    print(cat.eat())
    print(cat.meow())

    dog = Dog()
    print(dog.eat())
    print(dog.bark())

    try:
        print(cat.bark())
    except AttributeError:
        print("Cats don't bark...")

    try:
        print(dog.meow())
    except AttributeError:
        print("Dogs don't meow...")


if __name__ == "__main__":
    main()

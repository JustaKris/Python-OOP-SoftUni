# from project.animal import Animal
from project.mammal import Mammal
from project.lizard import Lizard


def main():
    mammal = Mammal("Stella")
    print(mammal.__class__.__bases__[0].__name__)
    print(mammal.name)
    lizard = Lizard("John")
    print(lizard.__class__.__bases__[0].__name__)
    print(lizard.name)


if __name__ == "__main__":
    main()

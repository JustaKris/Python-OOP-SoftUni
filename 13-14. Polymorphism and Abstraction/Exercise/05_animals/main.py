from project.dog import Dog
from project.cat import Cat
from project.tomcat import Tomcat
from project.kitten import Kitten


def main():
    # Test 1
    dog = Dog("Rocky", 3, "Male")
    print(dog.make_sound())
    print(dog)
    tomcat = Tomcat("Tom", 6)
    print(tomcat.make_sound())
    print(tomcat)

    # Test 2
    kitten = Kitten("Kiki", 1)
    print(kitten.make_sound())
    print(kitten)
    cat = Cat("Johnny", 7, "Male")
    print(cat.make_sound())
    print(cat)


if __name__ == '__main__':
    main()

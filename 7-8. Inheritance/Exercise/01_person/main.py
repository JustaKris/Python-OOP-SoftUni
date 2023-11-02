from project.child import Child
from project.person import Person


def main():
    person = Person("Beelzebub", 666)
    print(person.name)
    print(person.age)

    child = Child("Beelzebub junior", 6)
    print(child.__class__.__bases__[0].__name__)
    print(child.name)
    print(child.age)


if __name__ == "__main__":
    main()

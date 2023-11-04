from person import Person


def main():
    person = Person("George", 32)
    print(person.get_name())
    print(person.get_age())


if __name__ == "__main__":
    main()

from groups import Group, Person


def main():
    p0 = Person('Aliko', 'Dangote')
    p1 = Person('Bill', 'Gates')
    p2 = Person('Warren', 'Buffet')
    p3 = Person('Elon', 'Musk')
    p4 = p2 + p3
    first_group = Group('__VIP__', [p0, p1, p2])
    second_group = Group('Special', [p3, p4])
    third_group = first_group + second_group
    print(len(first_group))
    print(second_group)
    print(third_group[0])
    for person in third_group:
        print(person)


if __name__ == '__main__':
    main()

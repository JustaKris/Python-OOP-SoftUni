from image_area import ImageArea


def main():
    # Test 1
    a1 = ImageArea(7, 10)
    a2 = ImageArea(35, 2)
    a3 = ImageArea(8, 9)
    print(a1 == a2)
    print(a1 != a3)

    # Test 2
    a1 = ImageArea(7, 10)
    a2 = ImageArea(35, 2)
    a3 = ImageArea(8, 9)
    print(a1 != a2)
    print(a1 >= a3)

    # Test 3
    a1 = ImageArea(7, 10)
    a2 = ImageArea(35, 2)
    a3 = ImageArea(8, 9)
    print(a1 <= a2)
    print(a1 < a3)


if __name__ == '__main__':
    main()

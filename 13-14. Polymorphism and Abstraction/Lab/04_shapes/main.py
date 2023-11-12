from shapes import Circle, Rectangle


def main():
    # Test 1
    circle = Circle(5)
    print(circle.calculate_area())
    print(circle.calculate_perimeter())

    # Test 2
    rectangle = Rectangle(10, 20)
    print(rectangle.calculate_area())
    print(rectangle.calculate_perimeter())


if __name__ == '__main__':
    main()

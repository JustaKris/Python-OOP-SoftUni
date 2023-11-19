from shapes import AreaCalculator, Rectangle, Triangle


def main():
    shapes = [Rectangle(1, 6), Triangle(2, 3)]
    calculator = AreaCalculator(shapes)
    print("The total area is: ", calculator.total_area)


if __name__ == '__main__':
    main()

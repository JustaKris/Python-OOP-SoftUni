from vehicle import Car, Truck


def main():
    # Test 1
    car = Car(20, 5)
    car.drive(3)
    print(car.fuel_quantity)
    car.refuel(10)
    print(car.fuel_quantity)

    # Test 2
    truck = Truck(100, 15)
    truck.drive(5)
    print(truck.fuel_quantity)
    truck.refuel(50)
    print(truck.fuel_quantity)


if __name__ == '__main__':
    main()
